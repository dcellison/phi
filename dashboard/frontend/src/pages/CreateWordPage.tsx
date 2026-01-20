import { useState } from 'react'
import { Check, X, AlertTriangle } from 'lucide-react'
import { Input } from '@/components/ui/input'
import { Button } from '@/components/ui/button'
import { Badge } from '@/components/ui/badge'
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from '@/components/ui/card'
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select'
import { Separator } from '@/components/ui/separator'
import { api, type ValidationResult, PILLAR_NAMES } from '@/lib/utils'

const POS_OPTIONS = ['noun', 'verb', 'adjective', 'particle', 'pronoun', 'preposition', 'conjunction', 'quantifier']

const SUBCATEGORY_OPTIONS = [
  'particle', 'pronoun', 'preposition', 'conjunction', 'quantifier', 'classifier', 'discourse', 'interrogative'
]

export default function CreateWordPage() {
  const [word, setWord] = useState('')
  const [gloss, setGloss] = useState('')
  const [validation, setValidation] = useState<ValidationResult | null>(null)
  const [category, setCategory] = useState('content')
  const [subcategory, setSubcategory] = useState('')
  const [selectedPos, setSelectedPos] = useState<string[]>([])
  const [concept, setConcept] = useState('')
  const [description, setDescription] = useState('')
  const [soundSymbolism, setSoundSymbolism] = useState('')
  const [grammaticalNotes, setGrammaticalNotes] = useState('')
  const [pillars, setPillars] = useState<Record<string, string>>({})
  const [submitting, setSubmitting] = useState(false)
  const [success, setSuccess] = useState<string | null>(null)
  const [error, setError] = useState<string | null>(null)

  const validateWord = async (value: string) => {
    if (!value.trim()) {
      setValidation(null)
      return
    }
    try {
      const result = await api<ValidationResult>('/validate', {
        method: 'POST',
        body: JSON.stringify({ word: value }),
      })
      setValidation(result)
    } catch (e) {
      console.error('Validation failed:', e)
    }
  }

  const togglePos = (pos: string) => {
    setSelectedPos((prev) =>
      prev.includes(pos) ? prev.filter((p) => p !== pos) : [...prev, pos]
    )
  }

  const updatePillar = (key: string, value: string) => {
    setPillars((prev) => ({ ...prev, [key]: value }))
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setSuccess(null)
    setError(null)

    if (!validation?.valid) {
      setError('Please enter a valid Phi word')
      return
    }

    if (selectedPos.length === 0) {
      setError('Please select at least one part of speech')
      return
    }

    const filledPillars = Object.fromEntries(
      Object.entries(pillars).filter(([_, v]) => v.trim())
    )

    if (Object.keys(filledPillars).length === 0) {
      setError('Please provide at least one philosophical pillar')
      return
    }

    setSubmitting(true)

    try {
      const result = await api<{ success: boolean; word: string }>('/words', {
        method: 'POST',
        body: JSON.stringify({
          word,
          gloss,
          pos: selectedPos,
          concept,
          description,
          sound_symbolism: soundSymbolism,
          grammatical_notes: grammaticalNotes || undefined,
          pillars: filledPillars,
          category,
          subcategory: category === 'function' ? subcategory : undefined,
        }),
      })

      if (result.success) {
        setSuccess(`Word "${result.word}" created successfully!`)
        // Reset form
        setWord('')
        setGloss('')
        setValidation(null)
        setSelectedPos([])
        setConcept('')
        setDescription('')
        setSoundSymbolism('')
        setGrammaticalNotes('')
        setPillars({})
      }
    } catch (e: any) {
      setError(e.message || 'Failed to create word')
    }

    setSubmitting(false)
  }

  return (
    <div className="p-6 max-w-4xl">
      <div className="mb-6">
        <h2 className="text-2xl font-light text-primary">Create New Word</h2>
        <p className="text-sm text-muted-foreground mt-1">
          Add a new vocabulary entry to the Phi lexicon
        </p>
      </div>

      <form onSubmit={handleSubmit}>
        <Card className="mb-6">
          <CardHeader>
            <CardTitle className="text-lg">Word Details</CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="grid grid-cols-2 gap-4">
              <div>
                <label className="text-sm font-medium mb-2 block">
                  Phi Word *
                </label>
                <Input
                  placeholder="e.g., phialu"
                  value={word}
                  onChange={(e) => {
                    setWord(e.target.value)
                    validateWord(e.target.value)
                  }}
                />
                {validation && (
                  <div className="mt-2 flex items-center gap-2 text-sm">
                    {validation.valid ? (
                      <>
                        <Check className="h-4 w-4 text-green-600" />
                        <span className="text-green-600">Valid word</span>
                      </>
                    ) : (
                      <>
                        <X className="h-4 w-4 text-destructive" />
                        <span className="text-destructive">
                          {validation.errors.join('; ')}
                        </span>
                      </>
                    )}
                  </div>
                )}
                {validation?.warnings && validation.warnings.length > 0 && (
                  <div className="mt-1 flex items-center gap-2 text-sm text-yellow-600">
                    <AlertTriangle className="h-4 w-4" />
                    {validation.warnings.join('; ')}
                  </div>
                )}
              </div>

              <div>
                <label className="text-sm font-medium mb-2 block">
                  English Gloss *
                </label>
                <Input
                  placeholder="e.g., water"
                  value={gloss}
                  onChange={(e) => setGloss(e.target.value)}
                />
              </div>
            </div>

            <div className="grid grid-cols-2 gap-4">
              <div>
                <label className="text-sm font-medium mb-2 block">
                  IPA (auto-generated)
                </label>
                <Input
                  value={validation?.ipa || ''}
                  readOnly
                  className="bg-muted"
                />
              </div>

              <div>
                <label className="text-sm font-medium mb-2 block">
                  Syllables (auto-parsed)
                </label>
                <Input
                  value={validation?.syllables?.join(', ') || ''}
                  readOnly
                  className="bg-muted"
                />
              </div>
            </div>

            <div className="grid grid-cols-2 gap-4">
              <div>
                <label className="text-sm font-medium mb-2 block">
                  Category *
                </label>
                <Select value={category} onValueChange={setCategory}>
                  <SelectTrigger>
                    <SelectValue />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="content">Content Word</SelectItem>
                    <SelectItem value="function">Function Word</SelectItem>
                    <SelectItem value="interjection">Interjection</SelectItem>
                  </SelectContent>
                </Select>
              </div>

              {category === 'function' && (
                <div>
                  <label className="text-sm font-medium mb-2 block">
                    Subcategory *
                  </label>
                  <Select value={subcategory} onValueChange={setSubcategory}>
                    <SelectTrigger>
                      <SelectValue placeholder="Select..." />
                    </SelectTrigger>
                    <SelectContent>
                      {SUBCATEGORY_OPTIONS.map((sub) => (
                        <SelectItem key={sub} value={sub}>
                          {sub.charAt(0).toUpperCase() + sub.slice(1)}
                        </SelectItem>
                      ))}
                    </SelectContent>
                  </Select>
                </div>
              )}
            </div>

            <div>
              <label className="text-sm font-medium mb-2 block">
                Parts of Speech *
              </label>
              <div className="flex flex-wrap gap-2">
                {POS_OPTIONS.map((pos) => (
                  <Badge
                    key={pos}
                    variant={selectedPos.includes(pos) ? 'default' : 'outline'}
                    className="cursor-pointer"
                    onClick={() => togglePos(pos)}
                  >
                    {pos}
                  </Badge>
                ))}
              </div>
            </div>
          </CardContent>
        </Card>

        <Card className="mb-6">
          <CardHeader>
            <CardTitle className="text-lg">Semantic Content</CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <div>
              <label className="text-sm font-medium mb-2 block">
                Concept *
              </label>
              <Input
                placeholder="e.g., Water / Life-flow / Essential fluid"
                value={concept}
                onChange={(e) => setConcept(e.target.value)}
              />
            </div>

            <div>
              <label className="text-sm font-medium mb-2 block">
                Description *
              </label>
              <textarea
                className="w-full min-h-[100px] rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
                placeholder="Full description of the concept..."
                value={description}
                onChange={(e) => setDescription(e.target.value)}
              />
            </div>

            <div>
              <label className="text-sm font-medium mb-2 block">
                Sound Symbolism *
              </label>
              <textarea
                className="w-full min-h-[80px] rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
                placeholder="How the sounds embody the meaning..."
                value={soundSymbolism}
                onChange={(e) => setSoundSymbolism(e.target.value)}
              />
            </div>

            <div>
              <label className="text-sm font-medium mb-2 block">
                Grammatical Notes
              </label>
              <textarea
                className="w-full min-h-[60px] rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
                placeholder="Usage patterns, syntactic behavior... (optional)"
                value={grammaticalNotes}
                onChange={(e) => setGrammaticalNotes(e.target.value)}
              />
            </div>
          </CardContent>
        </Card>

        <Card className="mb-6">
          <CardHeader>
            <CardTitle className="text-lg">Philosophical Pillars</CardTitle>
            <CardDescription>
              Provide at least one pillar connection
            </CardDescription>
          </CardHeader>
          <CardContent className="space-y-4">
            {Object.entries(PILLAR_NAMES).map(([key, name]) => (
              <div key={key}>
                <label className="text-sm font-medium mb-2 block">
                  {name}
                </label>
                <textarea
                  className="w-full min-h-[60px] rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
                  placeholder={`Connection to ${name.toLowerCase()}...`}
                  value={pillars[key] || ''}
                  onChange={(e) => updatePillar(key, e.target.value)}
                />
              </div>
            ))}
          </CardContent>
        </Card>

        <Separator className="my-6" />

        {error && (
          <div className="mb-4 p-4 bg-destructive/10 text-destructive rounded-md text-sm">
            {error}
          </div>
        )}

        {success && (
          <div className="mb-4 p-4 bg-green-100 text-green-800 dark:bg-green-900/20 dark:text-green-400 rounded-md text-sm">
            {success}
          </div>
        )}

        <div className="flex gap-4">
          <Button type="submit" disabled={submitting}>
            {submitting ? 'Creating...' : 'Create Word'}
          </Button>
          <Button
            type="button"
            variant="outline"
            onClick={() => {
              setWord('')
              setGloss('')
              setValidation(null)
              setSelectedPos([])
              setConcept('')
              setDescription('')
              setSoundSymbolism('')
              setGrammaticalNotes('')
              setPillars({})
              setError(null)
              setSuccess(null)
            }}
          >
            Reset
          </Button>
        </div>
      </form>
    </div>
  )
}
