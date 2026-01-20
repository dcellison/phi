import { type ClassValue, clsx } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

// API helper
const API_BASE = '/api'

export async function api<T>(endpoint: string, options?: RequestInit): Promise<T> {
  const response = await fetch(`${API_BASE}${endpoint}`, {
    ...options,
    headers: {
      'Content-Type': 'application/json',
      ...options?.headers,
    },
  })

  if (!response.ok) {
    const error = await response.json().catch(() => ({ detail: 'Unknown error' }))
    throw new Error(error.detail || 'Request failed')
  }

  return response.json()
}

// Types
export interface Word {
  id: number
  word: string
  gloss: string
  ipa: string
  pos: string[]
  concept: string
  category: string
  subcategory: string | null
}

export interface WordDetail extends Word {
  syllables: string[]
  slot: number | null
  description: string
  sound_symbolism: string
  grammatical_notes: string | null
  image_prompt: string | null
  pillars: Record<string, string>
  tags: Record<string, string> | null
  source_file: string
}

export interface WordsResponse {
  words: Word[]
  total: number
  limit: number
  offset: number
}

export interface Stats {
  total: number
  by_category: Record<string, number>
  by_pos: Record<string, number>
  function_subcategories: Record<string, number>
}

export interface Particle {
  word: string
  gloss: string
  ipa: string
  slot: number | null
  concept: string
  description: string
}

export interface ParticlesResponse {
  '0': Particle[]
  '1': Particle[]
  '2': Particle[]
}

export interface GrammarDoc {
  name: string
  title: string
  path: string
}

export interface GrammarContent {
  title: string
  content: string
  raw: string
}

export interface ValidationResult {
  valid: boolean
  errors: string[]
  warnings: string[]
  syllables: string[]
  ipa?: string
}

// Pillar display names
export const PILLAR_NAMES: Record<string, string> = {
  'solarpunk-values': 'Solarpunk Values',
  'secular-buddhist-philosophy': 'Secular Buddhist Philosophy',
  'art-nouveau-aesthetics': 'Art Nouveau Aesthetics',
  'peace-linguistics-practices': 'Peace Linguistics',
  'pre-industrial-wisdom': 'Pre-Industrial Wisdom',
}

// Semantic domain tags
export const SEMANTIC_TAGS: { value: string; label: string; description: string }[] = [
  { value: 'nature', label: 'Nature', description: 'Natural world, environment, ecology' },
  { value: 'community', label: 'Community', description: 'Relationships, social bonds, collective' },
  { value: 'wisdom', label: 'Wisdom', description: 'Understanding, awareness, knowledge' },
  { value: 'creation', label: 'Creation', description: 'Making, building, artistic expression' },
  { value: 'dialogue', label: 'Dialogue', description: 'Communication, expression, listening' },
  { value: 'temporal', label: 'Temporal', description: 'Time, change, transformation' },
  { value: 'aesthetic', label: 'Aesthetic', description: 'Beauty, harmony, sensory appreciation' },
  { value: 'emotion', label: 'Emotion', description: 'Feeling states, emotional experiences' },
  { value: 'physical', label: 'Physical', description: 'Bodily experiences, tangible qualities' },
  { value: 'ritual', label: 'Ritual', description: 'Ceremony, tradition, sacred practices' },
  { value: 'cognition', label: 'Cognition', description: 'Mental processes, thinking, reasoning' },
  { value: 'spatial', label: 'Spatial', description: 'Location, movement, direction' },
  { value: 'activity', label: 'Activity', description: 'Actions, verbs of doing, basic human activities' },
]
