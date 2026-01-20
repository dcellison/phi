import { useState, useEffect, useCallback } from 'react'
import { Search, ChevronLeft, ChevronRight, ChevronsLeft, ChevronsRight, Pencil, Save, X } from 'lucide-react'
import { Input } from '@/components/ui/input'
import { Button } from '@/components/ui/button'
import { Badge } from '@/components/ui/badge'
import { Card, CardContent } from '@/components/ui/card'
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select'
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
} from '@/components/ui/dialog'
import { ScrollArea } from '@/components/ui/scroll-area'
import { Separator } from '@/components/ui/separator'
import { api, type Word, type WordDetail, type WordsResponse, PILLAR_NAMES, SEMANTIC_TAGS } from '@/lib/utils'

const POS_OPTIONS = [
  { value: '', label: 'All Parts of Speech' },
  { value: 'noun', label: 'Noun' },
  { value: 'verb', label: 'Verb' },
  { value: 'adjective', label: 'Adjective' },
  { value: 'particle', label: 'Particle' },
  { value: 'pronoun', label: 'Pronoun' },
  { value: 'preposition', label: 'Preposition' },
  { value: 'conjunction', label: 'Conjunction' },
  { value: 'quantifier', label: 'Quantifier' },
  { value: 'complementizer', label: 'Complementizer' },
  { value: 'vocative', label: 'Vocative' },
  { value: 'interjection', label: 'Interjection' },
]

const ALL_POS = ['noun', 'verb', 'adjective', 'particle', 'pronoun', 'preposition', 'conjunction', 'quantifier', 'complementizer', 'vocative', 'interjection']


// Editable text field component
function EditableField({
  label,
  value,
  editing,
  onChange,
  multiline = false,
  italic = false,
  className = '',
}: {
  label: string
  value: string | undefined
  editing: boolean
  onChange: (value: string) => void
  multiline?: boolean
  italic?: boolean
  className?: string
}) {
  if (editing) {
    return (
      <div>
        <h4 className="text-xs uppercase tracking-wider text-muted-foreground mb-1">
          {label}
        </h4>
        {multiline ? (
          <textarea
            className="w-full min-h-[80px] rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
            value={value || ''}
            onChange={(e) => onChange(e.target.value)}
          />
        ) : (
          <Input
            value={value || ''}
            onChange={(e) => onChange(e.target.value)}
          />
        )}
      </div>
    )
  }

  return (
    <div className={className}>
      <h4 className="text-xs uppercase tracking-wider text-muted-foreground mb-1">
        {label}
      </h4>
      <p className={`${italic ? 'italic' : ''} ${multiline ? 'text-sm leading-relaxed' : ''}`}>
        {value || <span className="text-muted-foreground/50">Not set</span>}
      </p>
    </div>
  )
}

// Editable POS badges
function EditablePOS({
  value,
  editing,
  onChange,
}: {
  value: string[]
  editing: boolean
  onChange: (value: string[]) => void
}) {
  const togglePos = (pos: string) => {
    if (value.includes(pos)) {
      onChange(value.filter((p) => p !== pos))
    } else {
      onChange([...value, pos])
    }
  }

  return (
    <div>
      <h4 className="text-xs uppercase tracking-wider text-muted-foreground mb-2">
        Parts of Speech
      </h4>
      <div className="flex flex-wrap gap-2">
        {editing ? (
          ALL_POS.map((p) => (
            <Badge
              key={p}
              variant={value.includes(p) ? 'default' : 'outline'}
              className="cursor-pointer"
              onClick={() => togglePos(p)}
            >
              {p}
            </Badge>
          ))
        ) : (
          value.map((p) => (
            <Badge key={p}>{p}</Badge>
          ))
        )}
      </div>
    </div>
  )
}

// Editable pillar field
function EditablePillar({
  pillarKey,
  value,
  editing,
  onChange,
}: {
  pillarKey: string
  value: string | undefined
  editing: boolean
  onChange: (value: string) => void
}) {
  if (editing) {
    return (
      <div className="border-l-2 border-primary/30 pl-3 py-1">
        <div className="text-sm font-medium text-primary mb-1">
          {PILLAR_NAMES[pillarKey] || pillarKey}
        </div>
        <textarea
          className="w-full min-h-[60px] rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
          value={value || ''}
          onChange={(e) => onChange(e.target.value)}
          placeholder={`Connection to ${(PILLAR_NAMES[pillarKey] || pillarKey).toLowerCase()}...`}
        />
      </div>
    )
  }

  if (!value) return null

  return (
    <div className="border-l-2 border-primary/30 pl-3 py-1">
      <div className="text-sm font-medium text-primary">
        {PILLAR_NAMES[pillarKey] || pillarKey}
      </div>
      <p className="text-sm text-muted-foreground mt-1">{value}</p>
    </div>
  )
}

// Editable semantic domain tags
function EditableTags({
  value,
  editing,
  onChange,
}: {
  value: string[]
  editing: boolean
  onChange: (value: string[]) => void
}) {
  const toggleTag = (tag: string) => {
    if (value.includes(tag)) {
      onChange(value.filter((t) => t !== tag))
    } else {
      onChange([...value, tag])
    }
  }

  return (
    <div>
      <h4 className="text-xs uppercase tracking-wider text-muted-foreground mb-2">
        Semantic Domain Tags
      </h4>
      {editing ? (
        <div className="flex flex-wrap gap-2">
          {SEMANTIC_TAGS.map((tag) => (
            <Badge
              key={tag.value}
              variant={value.includes(tag.value) ? 'default' : 'outline'}
              className="cursor-pointer"
              onClick={() => toggleTag(tag.value)}
              title={tag.description}
            >
              {tag.label}
            </Badge>
          ))}
        </div>
      ) : value.length > 0 ? (
        <div className="flex flex-wrap gap-2">
          {value.map((tag) => {
            const tagInfo = SEMANTIC_TAGS.find((t) => t.value === tag)
            return (
              <Badge key={tag} variant="outline" title={tagInfo?.description}>
                {tagInfo?.label || tag}
              </Badge>
            )
          })}
        </div>
      ) : (
        <p className="text-sm text-muted-foreground/50">No tags assigned</p>
      )}
    </div>
  )
}

export default function VocabularyPage() {
  const [words, setWords] = useState<Word[]>([])
  const [total, setTotal] = useState(0)
  const [loading, setLoading] = useState(true)
  const [search, setSearch] = useState('')
  const [pos, setPos] = useState('')
  const [sortBy, setSortBy] = useState<'gloss' | 'word'>('gloss')
  const [offset, setOffset] = useState(0)
  const [selectedWord, setSelectedWord] = useState<WordDetail | null>(null)
  const [dialogOpen, setDialogOpen] = useState(false)

  // Edit mode state
  const [editing, setEditing] = useState(false)
  const [editData, setEditData] = useState<Partial<WordDetail>>({})
  const [saving, setSaving] = useState(false)
  const [saveError, setSaveError] = useState<string | null>(null)

  const limit = 50

  const loadWords = useCallback(async () => {
    setLoading(true)
    try {
      const params = new URLSearchParams({
        limit: String(limit),
        offset: String(offset),
        sort: sortBy,
      })
      if (search) params.set('search', search)
      if (pos) params.set('pos', pos)

      const data = await api<WordsResponse>(`/words?${params}`)
      setWords(data.words)
      setTotal(data.total)
    } catch (e) {
      console.error('Failed to load words:', e)
    }
    setLoading(false)
  }, [search, pos, sortBy, offset])

  useEffect(() => {
    loadWords()
  }, [loadWords])

  useEffect(() => {
    setOffset(0)
  }, [search, pos, sortBy])

  const loadWordDetail = async (word: string) => {
    try {
      const data = await api<WordDetail>(`/words/${word}`)
      setSelectedWord(data)
      setEditData({})
      setEditing(false)
      setSaveError(null)
      setDialogOpen(true)
    } catch (e) {
      console.error('Failed to load word detail:', e)
    }
  }

  // Helper to convert tags object to array of tag names
  const tagsToArray = (tags: Record<string, string> | null): string[] => {
    if (!tags) return []
    return Object.keys(tags)
  }

  // Helper to convert array of tag names to tags object
  const arrayToTags = (arr: string[]): Record<string, string> => {
    const result: Record<string, string> = {}
    arr.forEach((tag) => {
      result[tag] = 'true'
    })
    return result
  }

  const startEditing = () => {
    if (selectedWord) {
      setEditData({
        gloss: selectedWord.gloss,
        concept: selectedWord.concept,
        description: selectedWord.description,
        sound_symbolism: selectedWord.sound_symbolism,
        grammatical_notes: selectedWord.grammatical_notes || '',
        pos: [...selectedWord.pos],
        pillars: { ...selectedWord.pillars },
        tags: selectedWord.tags ? { ...selectedWord.tags } : {},
      })
      setEditing(true)
      setSaveError(null)
    }
  }

  const cancelEditing = () => {
    setEditing(false)
    setEditData({})
    setSaveError(null)
  }

  const saveChanges = async () => {
    if (!selectedWord) return

    setSaving(true)
    setSaveError(null)

    try {
      await api(`/words/${selectedWord.word}`, {
        method: 'PUT',
        body: JSON.stringify(editData),
      })

      // Reload the word detail to get updated data
      const data = await api<WordDetail>(`/words/${selectedWord.word}`)
      setSelectedWord(data)
      setEditing(false)
      setEditData({})

      // Reload the word list to reflect any changes
      loadWords()
    } catch (e: any) {
      setSaveError(e.message || 'Failed to save changes')
    }

    setSaving(false)
  }

  const updateEditField = (field: keyof WordDetail, value: any) => {
    setEditData((prev) => ({ ...prev, [field]: value }))
  }

  const updatePillar = (key: string, value: string) => {
    setEditData((prev) => ({
      ...prev,
      pillars: { ...(prev.pillars || selectedWord?.pillars || {}), [key]: value },
    }))
  }

  const updateTags = (tagArray: string[]) => {
    setEditData((prev) => ({
      ...prev,
      tags: arrayToTags(tagArray),
    }))
  }

  const totalPages = Math.ceil(total / limit)
  const currentPage = Math.floor(offset / limit) + 1

  // Get display values (edit data if editing, otherwise selected word)
  const displayGloss = editing ? editData.gloss : selectedWord?.gloss
  const displayConcept = editing ? editData.concept : selectedWord?.concept
  const displayDescription = editing ? editData.description : selectedWord?.description
  const displaySoundSymbolism = editing ? editData.sound_symbolism : selectedWord?.sound_symbolism
  const displayGrammaticalNotes = editing ? editData.grammatical_notes : selectedWord?.grammatical_notes
  const displayPos = editing ? (editData.pos || []) : (selectedWord?.pos || [])
  const displayPillars = editing ? (editData.pillars || {}) : (selectedWord?.pillars || {})
  const displayTags = editing ? tagsToArray(editData.tags || null) : tagsToArray(selectedWord?.tags || null)

  return (
    <div className="p-6">
      <div className="flex items-center justify-between mb-6">
        <h2 className="text-2xl font-light text-primary">Vocabulary</h2>
        <div className="text-sm text-muted-foreground">
          {total} words
        </div>
      </div>

      {/* Filters */}
      <div className="flex flex-wrap gap-4 mb-6">
        <div className="relative flex-1 min-w-[200px] max-w-sm">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-muted-foreground" />
          <Input
            placeholder="Search words, glosses, concepts..."
            className="pl-9"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
          />
        </div>

        <Select value={pos || "all"} onValueChange={(v) => setPos(v === "all" ? "" : v)}>
          <SelectTrigger className="w-[200px]">
            <SelectValue placeholder="All Parts of Speech" />
          </SelectTrigger>
          <SelectContent>
            {POS_OPTIONS.map((opt) => (
              <SelectItem key={opt.value || "all"} value={opt.value || "all"}>
                {opt.label}
              </SelectItem>
            ))}
          </SelectContent>
        </Select>

        <Select value={sortBy} onValueChange={(v) => setSortBy(v as 'gloss' | 'word')}>
          <SelectTrigger className="w-[160px]">
            <SelectValue />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="gloss">Sort by Gloss</SelectItem>
            <SelectItem value="word">Sort by Phi Word</SelectItem>
          </SelectContent>
        </Select>
      </div>

      {/* Word List */}
      <div className="space-y-2">
        {loading ? (
          <div className="text-center py-12 text-muted-foreground">
            Loading...
          </div>
        ) : words.length === 0 ? (
          <div className="text-center py-12 text-muted-foreground">
            No words found
          </div>
        ) : (
          words.map((word) => (
            <Card
              key={word.id}
              className="cursor-pointer hover:bg-muted/50 transition-colors"
              onClick={() => loadWordDetail(word.word)}
            >
              <CardContent className="p-4">
                <div className="flex items-center gap-4">
                  <div className="w-32">
                    <span className="text-lg font-medium text-primary">
                      {word.word}
                    </span>
                  </div>
                  <div className="w-24 text-muted-foreground italic">
                    {word.gloss}
                  </div>
                  <div className="flex-1 text-sm truncate">
                    {word.concept}
                  </div>
                  <div className="flex gap-1">
                    {word.pos.map((p) => (
                      <Badge key={p} variant="secondary" className="text-xs">
                        {p}
                      </Badge>
                    ))}
                  </div>
                </div>
              </CardContent>
            </Card>
          ))
        )}
      </div>

      {/* Pagination */}
      {totalPages > 1 && (
        <div className="flex items-center justify-center gap-1 mt-6">
          <Button
            variant="outline"
            size="sm"
            onClick={() => setOffset(0)}
            disabled={currentPage === 1}
            title="First page"
          >
            <ChevronsLeft className="h-4 w-4" />
          </Button>
          <Button
            variant="outline"
            size="sm"
            onClick={() => setOffset(Math.max(0, offset - limit))}
            disabled={currentPage === 1}
            title="Previous page"
          >
            <ChevronLeft className="h-4 w-4" />
          </Button>

          {/* Page numbers */}
          <div className="flex items-center gap-1 mx-2">
            {(() => {
              const pages: (number | string)[] = []
              const maxVisible = 6 // Show up to 6 page numbers (plus ellipsis)

              if (totalPages <= maxVisible + 1) {
                // Show all pages if 7 or fewer
                for (let i = 1; i <= totalPages; i++) pages.push(i)
              } else if (currentPage <= maxVisible - 1) {
                // Near the start: show first pages + ellipsis + last
                for (let i = 1; i <= maxVisible; i++) pages.push(i)
                pages.push('...')
                pages.push(totalPages)
              } else {
                // Past the start: show first + ellipsis + pages ending at current + 1
                pages.push(1)
                pages.push('...')
                const startPage = Math.min(currentPage - 1, totalPages - maxVisible + 1)
                for (let i = startPage; i <= Math.min(startPage + maxVisible - 1, totalPages); i++) {
                  pages.push(i)
                }
              }

              return pages.map((page, idx) =>
                typeof page === 'string' ? (
                  <span key={`ellipsis-${idx}`} className="px-2 text-muted-foreground">
                    {page}
                  </span>
                ) : (
                  <Button
                    key={page}
                    variant={page === currentPage ? 'default' : 'outline'}
                    size="sm"
                    className="w-9"
                    onClick={() => setOffset((page - 1) * limit)}
                  >
                    {page}
                  </Button>
                )
              )
            })()}
          </div>

          <Button
            variant="outline"
            size="sm"
            onClick={() => setOffset(offset + limit)}
            disabled={currentPage === totalPages}
            title="Next page"
          >
            <ChevronRight className="h-4 w-4" />
          </Button>
          <Button
            variant="outline"
            size="sm"
            onClick={() => setOffset((totalPages - 1) * limit)}
            disabled={currentPage === totalPages}
            title="Last page"
          >
            <ChevronsRight className="h-4 w-4" />
          </Button>
        </div>
      )}

      {/* Word Detail Dialog */}
      <Dialog open={dialogOpen} onOpenChange={(open) => {
        if (!open) {
          setEditing(false)
          setEditData({})
          setSaveError(null)
        }
        setDialogOpen(open)
      }}>
        <DialogContent className="max-w-2xl max-h-[90vh]">
          <DialogHeader>
            <div className="flex items-center justify-between">
              <DialogTitle className="flex items-baseline gap-3">
                <span className="text-3xl font-light text-primary">
                  {selectedWord?.word}
                </span>
                <span className="text-lg text-muted-foreground ipa">
                  {selectedWord?.ipa}
                </span>
              </DialogTitle>
              <div className="flex gap-2 mr-8">
                {editing ? (
                  <>
                    <Button
                      variant="ghost"
                      size="sm"
                      onClick={cancelEditing}
                      disabled={saving}
                    >
                      <X className="h-4 w-4 mr-1" />
                      Cancel
                    </Button>
                    <Button
                      size="sm"
                      onClick={saveChanges}
                      disabled={saving}
                    >
                      <Save className="h-4 w-4 mr-1" />
                      {saving ? 'Saving...' : 'Save'}
                    </Button>
                  </>
                ) : (
                  <Button
                    variant="ghost"
                    size="sm"
                    onClick={startEditing}
                  >
                    <Pencil className="h-4 w-4 mr-1" />
                    Edit
                  </Button>
                )}
              </div>
            </div>
          </DialogHeader>

          {saveError && (
            <div className="bg-destructive/10 text-destructive text-sm p-3 rounded-md">
              {saveError}
            </div>
          )}

          <ScrollArea className="max-h-[70vh] pr-4">
            {selectedWord && (
              <div className="space-y-6">
                <EditableField
                  label="Gloss"
                  value={displayGloss}
                  editing={editing}
                  onChange={(v) => updateEditField('gloss', v)}
                  italic
                />

                <EditableField
                  label="Concept"
                  value={displayConcept}
                  editing={editing}
                  onChange={(v) => updateEditField('concept', v)}
                />

                <EditablePOS
                  value={displayPos}
                  editing={editing}
                  onChange={(v) => updateEditField('pos', v)}
                />

                <div>
                  <h4 className="text-xs uppercase tracking-wider text-muted-foreground mb-1">
                    Syllables
                  </h4>
                  <p className="font-mono">
                    {selectedWord.syllables?.join(' · ')}
                  </p>
                </div>

                <Separator />

                <EditableField
                  label="Description"
                  value={displayDescription}
                  editing={editing}
                  onChange={(v) => updateEditField('description', v)}
                  multiline
                />

                <EditableField
                  label="Sound Symbolism"
                  value={displaySoundSymbolism}
                  editing={editing}
                  onChange={(v) => updateEditField('sound_symbolism', v)}
                  multiline
                  className="text-muted-foreground"
                />

                <EditableField
                  label="Grammatical Notes"
                  value={displayGrammaticalNotes || undefined}
                  editing={editing}
                  onChange={(v) => updateEditField('grammatical_notes', v)}
                  multiline
                />

                <Separator />

                <div>
                  <h4 className="text-xs uppercase tracking-wider text-muted-foreground mb-3">
                    Philosophical Pillars
                  </h4>
                  <div className="space-y-3">
                    {editing ? (
                      // Show all pillars when editing
                      Object.keys(PILLAR_NAMES).map((key) => (
                        <EditablePillar
                          key={key}
                          pillarKey={key}
                          value={displayPillars[key]}
                          editing={editing}
                          onChange={(v) => updatePillar(key, v)}
                        />
                      ))
                    ) : (
                      // Show only filled pillars when viewing
                      Object.entries(displayPillars)
                        .filter(([_, value]) => value)
                        .map(([key, value]) => (
                          <EditablePillar
                            key={key}
                            pillarKey={key}
                            value={value}
                            editing={false}
                            onChange={() => {}}
                          />
                        ))
                    )}
                  </div>
                </div>

                <EditableTags
                  value={displayTags}
                  editing={editing}
                  onChange={updateTags}
                />

                <Separator />

                <div className="text-xs text-muted-foreground">
                  Source: <code>{selectedWord.source_file}</code>
                </div>
              </div>
            )}
          </ScrollArea>
        </DialogContent>
      </Dialog>
    </div>
  )
}
