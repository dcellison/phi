#!/usr/bin/env python3
"""
Web API for Phi Sentence Validator

Simple Flask API for validating Phi sentences online.
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from phi_validation.core import PhiSentenceValidator

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend integration

# Initialize validator once at startup
validator = PhiSentenceValidator()

@app.route('/validate', methods=['POST'])
def validate_sentence():
    """Validate a Phi sentence and return detailed results."""
    try:
        data = request.get_json()
        
        if not data or 'sentence' not in data:
            return jsonify({
                'error': 'Missing sentence in request body',
                'example': {'sentence': 'mia ta whemo'}
            }), 400
        
        sentence = data['sentence'].strip()
        
        if not sentence:
            return jsonify({
                'error': 'Empty sentence provided'
            }), 400
        
        # Validate the sentence
        result = validator.validate_sentence(sentence)
        
        # Add glosses and translations for each token
        tokens_with_glosses = []
        sentence_translation_parts = []
        
        for token in result['tokens']:
            token_info = {
                'word': token.lower(),  # Ensure lowercase for words
                'gloss': None,
                'translation': None,
                'pos': None
            }
            
            # Look up word in lexicon
            if hasattr(validator.lexicon_validator.word_validator, 'lexicon'):
                lexicon = validator.lexicon_validator.word_validator.lexicon
                
                # Handle particles and common words using proper linguistic glosses FIRST
                particle_glosses = {
                    # Pronouns
                    'mia': '1SG', 'thi': '2SG', 'sha': '3SG',
                    
                    # Tense/Aspect (Slot 1)
                    'ta': 'PRS', 'li': 'PST', 'su': 'FUT',
                    'we': 'DES', 'to': 'IMP', 'ru': 'OBLG',
                    'la': 'PROG', 'ni': 'PRF', 'po': 'HAB',
                    'pu': 'PFV', 'ri': 'IPFV', 'wi': 'INCH', 'wu': 'CESS',
                    'me': 'NEG',
                    
                    # Animacy/Role markers (Slot 2)
                    'he': 'HUM', 'pi': 'ANIM', 'ne': 'INAN',
                    'na': 'OBJ', 'si': 'SUBJ', 'te': 'VRB',
                    
                    # Derivational
                    'se': 'NVERB', 'ra': 'VNOUN',
                    
                    # Emphasis/Number
                    'ma': 'EMPH', 'wo': 'PAUC', 'lo': 'PL', 'no': 'GPL',
                    
                    # Comparison
                    'pa': 'SPRL', 'mo': 'CMPR', 'sa': 'EQ', 'le': 'LESS', 're': 'LEAST',
                    
                    # Evidentiality (Slot 0)
                    'hi': 'DIR.EV', 'ro': 'INFR', 'nu': 'HRSY',
                    'ti': 'REP', 'mu': 'MEM', 'pe': 'PRES',
                    
                    # Sentence type/mood (Slot 0)
                    'wa': 'Q', 'ho': 'EXCL', 'tu': 'COND', 'hu': 'PSB',
                    'lu': 'REL',
                    
                    # Discourse (Slot 0)
                    'ha': 'TOP', 'mi': 'CNTR', 'so': 'POL',
                    
                    # Common copula
                    'phera': 'COP'
                }
                
                particle_translations = {
                    # Pronouns
                    'mia': 'I', 'thi': 'you', 'sha': 'they',
                    
                    # Tense/Aspect
                    'ta': '', 'li': '', 'su': 'will',  # Tense markers often don't translate directly
                    'we': 'want to', 'to': '', 'ru': 'must',
                    'la': '', 'ni': 'have', 'po': 'usually',
                    'pu': '', 'ri': '', 'wi': 'start to', 'wu': 'stop',
                    'me': 'not',
                    
                    # Animacy/Role markers (usually don't translate)
                    'he': '', 'pi': '', 'ne': '',
                    'na': '', 'si': '', 'te': '',
                    
                    # Derivational
                    'se': '', 'ra': '',
                    
                    # Emphasis/Number
                    'ma': '', 'wo': 'few', 'lo': '', 'no': 'many',
                    
                    # Comparison
                    'pa': 'most', 'mo': 'more', 'sa': 'as', 'le': 'less', 're': 'least',
                    
                    # Evidentiality
                    'hi': '', 'ro': 'apparently', 'nu': 'reportedly',
                    'ti': 'they say', 'mu': 'I remember', 'pe': 'presumably',
                    
                    # Sentence type/mood
                    'wa': '', 'ho': '', 'tu': 'if', 'hu': 'maybe',
                    'lu': '',
                    
                    # Discourse
                    'ha': '', 'mi': 'but', 'so': '',
                    
                    # Common copula
                    'phera': 'is'
                }
                
                # Check particles first
                if token.lower() in particle_glosses:
                    token_info['gloss'] = particle_glosses[token.lower()]
                    token_info['translation'] = particle_translations[token.lower()]
                    token_info['pos'] = 'particle' if token.lower() != 'phera' else 'verb'
                    # Only add to translation if it has content
                    if token_info['translation']:
                        sentence_translation_parts.append(token_info['translation'])
                else:
                    # Search through all parts of speech in main lexicon
                    found = False
                    for pos, word_entries in lexicon.items():
                        if isinstance(word_entries, list):
                            for entry in word_entries:
                                if hasattr(entry, 'word') and entry.word.lower() == token.lower():
                                    token_info['pos'] = entry.pos
                                    token_info['translation'] = entry.meaning
                                    # For content words, use the English translation as gloss (lowercase)
                                    token_info['gloss'] = entry.meaning.lower()
                                    sentence_translation_parts.append(entry.meaning)
                                    found = True
                                    break
                        if found:
                            break
                    
                    if not found:
                        token_info['gloss'] = token.lower()
                        token_info['translation'] = token
                        token_info['pos'] = 'unknown'
                        sentence_translation_parts.append(token)
            
            tokens_with_glosses.append(token_info)
        
        # Create interlinear gloss format
        words_line = ' '.join([token['word'] for token in tokens_with_glosses])
        glosses_line = ' '.join([token['gloss'] for token in tokens_with_glosses])
        translation_line = ' '.join([part for part in sentence_translation_parts if part])
        
        interlinear_gloss = {
            'words': words_line,
            'glosses': glosses_line,
            'translation': translation_line
        }
        
        # Convert errors to serializable format
        serializable_result = {
            'sentence': result['sentence'],
            'tokens': result['tokens'],
            'tokens_with_glosses': tokens_with_glosses,
            'is_valid': result['is_valid'],
            'error_count': len(result['actual_errors']),
            'warning_count': len(result['warnings']),
            'errors': [
                {
                    'type': error.error_type.value,
                    'message': error.message,
                    'position': error.position,
                    'word': error.word
                }
                for error in result['actual_errors']
            ],
            'warnings': [
                {
                    'type': warning.error_type.value,
                    'message': warning.message,
                    'position': warning.position,
                    'word': warning.word
                }
                for warning in result['warnings']
            ],
            'error_summary': result['error_summary'],
            'interlinear_gloss': interlinear_gloss
        }
        
        return jsonify(serializable_result)
    
    except Exception as e:
        return jsonify({
            'error': f'Internal server error: {str(e)}'
        }), 500

@app.route('/validate/batch', methods=['POST'])
def validate_batch():
    """Validate multiple sentences at once."""
    try:
        data = request.get_json()
        
        if not data or 'sentences' not in data:
            return jsonify({
                'error': 'Missing sentences array in request body',
                'example': {'sentences': ['mia ta whemo', 'thi ta whera']}
            }), 400
        
        sentences = data['sentences']
        
        if not isinstance(sentences, list):
            return jsonify({
                'error': 'Sentences must be an array'
            }), 400
        
        if len(sentences) > 100:  # Limit batch size
            return jsonify({
                'error': 'Batch size limited to 100 sentences'
            }), 400
        
        results = []
        for sentence in sentences:
            if isinstance(sentence, str) and sentence.strip():
                result = validator.validate_sentence(sentence.strip())
                results.append({
                    'sentence': result['sentence'],
                    'tokens': result['tokens'],
                    'is_valid': result['is_valid'],
                    'error_count': len(result['actual_errors']),
                    'errors': [
                        {
                            'type': error.error_type.value,
                            'message': error.message,
                            'position': error.position
                        }
                        for error in result['actual_errors']
                    ]
                })
            else:
                results.append({
                    'sentence': sentence,
                    'error': 'Invalid sentence format'
                })
        
        return jsonify({
            'results': results,
            'total_processed': len(results)
        })
    
    except Exception as e:
        return jsonify({
            'error': f'Internal server error: {str(e)}'
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'validator_loaded': validator is not None,
        'lexicon_size': len(validator.lexicon_validator.word_validator.lexicon) if validator else 0
    })

@app.route('/info', methods=['GET'])
def validator_info():
    """Get information about the validator."""
    return jsonify({
        'name': 'Phi Sentence Validator',
        'version': '1.0.0',
        'modules': [
            'lexicon', 'particles', 'word_order', 'temporal', 
            'semantic_roles', 'modality', 'evidentiality', 
            'derivational', 'emphasis', 'politeness', 
            'discourse', 'interrogative', 'narrative'
        ],
        'lexicon_size': len(validator.lexicon_validator.word_validator.lexicon),
        'supported_features': [
            'SOV word order validation',
            'Particle ordering and scope',
            'Temporal logic and tense consistency',
            'Animacy and semantic role validation',
            'Modal logic and conditionals',
            'Evidentiality systems',
            'Derivational constructions',
            'Emphasis and politeness markers',
            'Discourse structure',
            'Question formation',
            'Narrative sequences'
        ]
    })

@app.route('/', methods=['GET'])
def index():
    """API documentation."""
    return jsonify({
        'name': 'Phi Sentence Validator API',
        'version': '1.0.0',
        'endpoints': {
            'POST /validate': {
                'description': 'Validate a single Phi sentence',
                'body': {'sentence': 'string'},
                'example': {'sentence': 'mia ta whemo'}
            },
            'POST /validate/batch': {
                'description': 'Validate multiple sentences',
                'body': {'sentences': ['string']},
                'example': {'sentences': ['mia ta whemo', 'thi ta whera']}
            },
            'GET /health': {
                'description': 'Health check'
            },
            'GET /info': {
                'description': 'Validator information'
            }
        },
        'example_usage': {
            'curl': 'curl -X POST -H "Content-Type: application/json" -d \'{"sentence":"mia ta whemo"}\' http://localhost:8080/validate'
        }
    })

if __name__ == '__main__':
    print("Starting Phi Sentence Validator API...")
    print("Initializing validator...")
    
    # Test the validator on startup
    test_result = validator.validate_sentence("mia ta whemo")
    print(f"Startup test: {'✅ PASSED' if test_result['is_valid'] else '❌ FAILED'}")
    
    print("API ready at http://localhost:8080")
    print("Endpoints:")
    print("  POST /validate - validate single sentence")
    print("  POST /validate/batch - validate multiple sentences")
    print("  GET /health - health check")
    print("  GET /info - validator information")
    
    app.run(debug=True, host='0.0.0.0', port=8080) 