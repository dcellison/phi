import { useState, useEffect } from 'react'
import { Pencil, Save, X, BookOpen, Layers, MessageSquare } from 'lucide-react'
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs'
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
} from '@/components/ui/dialog'
import { ScrollArea } from '@/components/ui/scroll-area'
import { Separator } from '@/components/ui/separator'
import { api, type ParticlesResponse, type Particle, type WordDetail, PILLAR_NAMES, SEMANTIC_TAGS } from '@/lib/utils'

// Editable text field component
function EditableField({
  label,
  value,
  editing,
  onChange,
  multiline = false,
  italic = false,
}: {
  label: string
  value: string | undefined
  editing: boolean
  onChange: (value: string) => void
  multiline?: boolean
  italic?: boolean
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
    <div>
      <h4 className="text-xs uppercase tracking-wider text-muted-foreground mb-1">
        {label}
      </h4>
      <p className={`${italic ? 'italic' : ''} ${multiline ? 'text-sm leading-relaxed' : ''}`}>
        {value || <span className="text-muted-foreground/50">Not set</span>}
      </p>
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

function ParticleCard({ particle, onClick }: { particle: Particle; onClick: () => void }) {
  return (
    <div
      className="flex items-start gap-3 p-3 rounded-md hover:bg-muted/50 transition-colors cursor-pointer"
      onClick={onClick}
    >
      <div className="w-16">
        <span className="font-medium text-primary">{particle.word}</span>
      </div>
      <div className="w-12 text-sm text-muted-foreground ipa">
        {particle.ipa}
      </div>
      <div className="w-20 text-sm text-muted-foreground italic">
        {particle.gloss}
      </div>
      <div className="flex-1 text-sm">
        {particle.concept}
      </div>
    </div>
  )
}

// Example component for usage examples
function Example({ phi, gloss, translation }: { phi: string; gloss: string; translation: string }) {
  return (
    <div className="p-4 bg-muted rounded-md font-mono text-sm space-y-1">
      <div className="text-primary">{phi}</div>
      <div className="text-xs text-muted-foreground">{gloss}</div>
      <div className="text-sm not-italic font-sans">{translation}</div>
    </div>
  )
}

// Section component for documentation
function DocSection({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <div className="space-y-3">
      <h3 className="text-lg font-medium text-primary">{title}</h3>
      <div className="space-y-4 text-sm leading-relaxed">{children}</div>
    </div>
  )
}

export default function ParticlesPage() {
  const [particles, setParticles] = useState<ParticlesResponse | null>(null)
  const [loading, setLoading] = useState(true)
  const [selectedWord, setSelectedWord] = useState<WordDetail | null>(null)
  const [dialogOpen, setDialogOpen] = useState(false)

  // Edit mode state
  const [editing, setEditing] = useState(false)
  const [editData, setEditData] = useState<Partial<WordDetail>>({})
  const [saving, setSaving] = useState(false)
  const [saveError, setSaveError] = useState<string | null>(null)

  useEffect(() => {
    loadParticles()
  }, [])

  const loadParticles = async () => {
    try {
      const data = await api<ParticlesResponse>('/particles')
      setParticles(data)
    } catch (e) {
      console.error('Failed to load particles:', e)
    }
    setLoading(false)
  }

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

      // Reload the particles list to reflect any changes
      loadParticles()
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

  // Get display values (edit data if editing, otherwise selected word)
  const displayGloss = editing ? editData.gloss : selectedWord?.gloss
  const displayConcept = editing ? editData.concept : selectedWord?.concept
  const displayDescription = editing ? editData.description : selectedWord?.description
  const displaySoundSymbolism = editing ? editData.sound_symbolism : selectedWord?.sound_symbolism
  const displayGrammaticalNotes = editing ? editData.grammatical_notes : selectedWord?.grammatical_notes
  const displayPillars = editing ? (editData.pillars || {}) : (selectedWord?.pillars || {})
  const displayTags = editing ? tagsToArray(editData.tags || null) : tagsToArray(selectedWord?.tags || null)

  if (loading) {
    return (
      <div className="p-6">
        <div className="text-center py-12 text-muted-foreground">
          Loading...
        </div>
      </div>
    )
  }

  return (
    <div className="p-6">
      <div className="mb-6">
        <h2 className="text-2xl font-light text-primary">The Particle System</h2>
        <p className="text-sm text-muted-foreground mt-1">
          Phi's three-slot particle system: announcing grammatical intent before content
        </p>
      </div>

      <Tabs defaultValue="overview" className="space-y-6">
        <TabsList className="grid w-full grid-cols-3">
          <TabsTrigger value="overview" className="flex items-center gap-2">
            <BookOpen className="h-4 w-4" />
            Overview
          </TabsTrigger>
          <TabsTrigger value="reference" className="flex items-center gap-2">
            <Layers className="h-4 w-4" />
            Reference
          </TabsTrigger>
          <TabsTrigger value="usage" className="flex items-center gap-2">
            <MessageSquare className="h-4 w-4" />
            Usage Guide
          </TabsTrigger>
        </TabsList>

        {/* OVERVIEW TAB */}
        <TabsContent value="overview" className="space-y-6">
          <Card>
            <CardHeader>
              <CardTitle>The Philosophy of Particle Precedence</CardTitle>
              <CardDescription>
                Why Phi announces grammatical intent before content
              </CardDescription>
            </CardHeader>
            <CardContent className="prose max-w-none space-y-6">
              <DocSection title="Conscious Communication">
                <p>
                  Phi's particle system embodies a radical approach to grammar: all grammatical markers
                  must appear <em>before</em> the content they modify. This isn't merely a structural
                  choice—it's a philosophical commitment to transparent, mindful communication.
                </p>
                <p>
                  In many languages, intent is hidden in subtle intonation or discovered only at the
                  end of an utterance. In Phi, the speaker must first be mindful of their own intention,
                  and then present it transparently, allowing the listener to prepare themselves to
                  receive the coming information in the proper context.
                </p>
              </DocSection>

              <DocSection title="The Three-Slot Architecture">
                <p>
                  Particles are organized into three ordered "slots" that reflect different scales of
                  grammatical modification:
                </p>
                <div className="grid gap-4 mt-4">
                  <div className="p-4 border rounded-lg border-primary/30">
                    <div className="flex items-center gap-2 mb-2">
                      <Badge>Slot 0</Badge>
                      <span className="font-medium">Sentence Frame</span>
                    </div>
                    <p className="text-muted-foreground">
                      Announces the speaker's communicative intent for the entire utterance. Is this a
                      question? A command? A hypothetical? The listener knows immediately.
                    </p>
                  </div>
                  <div className="p-4 border rounded-lg border-primary/30">
                    <div className="flex items-center gap-2 mb-2">
                      <Badge>Slot 1</Badge>
                      <span className="font-medium">Verb Phrase</span>
                    </div>
                    <p className="text-muted-foreground">
                      Announces temporal, aspectual, evidential, and modal context <em>before</em> the
                      verb. Listeners understand when, how, and with what certainty an action occurs
                      before learning what the action is.
                    </p>
                  </div>
                  <div className="p-4 border rounded-lg border-primary/30">
                    <div className="flex items-center gap-2 mb-2">
                      <Badge>Slot 2</Badge>
                      <span className="font-medium">Word-Level</span>
                    </div>
                    <p className="text-muted-foreground">
                      Announces modifications to individual words: plurality, focus, comparison, deixis,
                      and social relationships. Even at the smallest scale, modifiers precede what they modify.
                    </p>
                  </div>
                </div>
              </DocSection>

              <DocSection title="The Grammar of Trust">
                <p>
                  By requiring speakers to declare their core intention at the outset of a sentence,
                  Phi eliminates a vast field of potential misunderstanding. There is no need to guess
                  at the speaker's motive or to decipher their tone. The intention is the first thing
                  spoken—a clear and unambiguous promise for the communication that follows.
                </p>
                <p>
                  This simple architectural rule fosters a radically different kind of dialogue, one
                  where speakers are encouraged to be more mindful of their own purpose and more
                  respectful of their listener's cognitive effort. It shifts the burden of interpretation
                  away from the listener and places the burden of clarity squarely on the speaker.
                </p>
              </DocSection>

              <DocSection title="Present Moment as Foundation">
                <p>
                  The present tense in Phi requires no marker at all. This is a profound philosophical
                  choice, grounding the language in a state of active presence. Unless otherwise
                  specified, all actions are assumed to be happening in the current moment.
                </p>
                <p>
                  To speak of the past or future requires a <em>deliberate act</em>—a conscious choice
                  to place a temporal signpost before the verb. This transforms every non-present
                  statement into a moment of self-awareness, a recognition of where one's mind has
                  chosen to focus.
                </p>
              </DocSection>

              <DocSection title="Verbs as Timeless Concepts">
                <p>
                  The verb itself—the core concept of an action—remains pure, stable, and unchanging
                  throughout all modifications. The word <em>shima</em> (to read) never changes its
                  form whether the reading happened yesterday, is happening now, or is merely possible.
                </p>
                <p>
                  The particles dance and shift around the stable verb, clothing it in the specific
                  context of the moment. This reflects a profound philosophical stance: that actions,
                  in their purest form, are timeless concepts. It is only our relationship to them
                  that is fluid and requires explicit clarification.
                </p>
              </DocSection>
            </CardContent>
          </Card>
        </TabsContent>

        {/* REFERENCE TAB */}
        <TabsContent value="reference" className="space-y-6">
          <div className="text-sm text-muted-foreground mb-4">
            Click any particle to view and edit its full definition.
          </div>

          {/* Slot 0 */}
          <Card>
            <CardHeader>
              <div className="flex items-center gap-2">
                <Badge>Slot 0</Badge>
                <CardTitle className="text-lg">Sentence Frame Particles</CardTitle>
              </div>
              <CardDescription>
                Appear at the very beginning of a sentence to announce communicative intent
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="space-y-1">
                {particles?.['0'].map((p) => (
                  <ParticleCard key={p.word} particle={p} onClick={() => loadWordDetail(p.word)} />
                ))}
                {particles?.['0'].length === 0 && (
                  <p className="text-sm text-muted-foreground py-4 text-center">
                    No particles in this slot
                  </p>
                )}
              </div>
            </CardContent>
          </Card>

          {/* Slot 1 */}
          <Card>
            <CardHeader>
              <div className="flex items-center gap-2">
                <Badge>Slot 1</Badge>
                <CardTitle className="text-lg">Verb Phrase Particles</CardTitle>
              </div>
              <CardDescription>
                Appear before the verb in strict order: Tense → Aspect → Voice → Evidentiality → Modality → Negation
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="space-y-1">
                {particles?.['1'].map((p) => (
                  <ParticleCard key={p.word} particle={p} onClick={() => loadWordDetail(p.word)} />
                ))}
                {particles?.['1'].length === 0 && (
                  <p className="text-sm text-muted-foreground py-4 text-center">
                    No particles in this slot
                  </p>
                )}
              </div>
            </CardContent>
          </Card>

          {/* Slot 2 */}
          <Card>
            <CardHeader>
              <div className="flex items-center gap-2">
                <Badge>Slot 2</Badge>
                <CardTitle className="text-lg">Word-Level Particles</CardTitle>
              </div>
              <CardDescription>
                Appear immediately before the specific word they modify
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="space-y-1">
                {particles?.['2'].map((p) => (
                  <ParticleCard key={p.word} particle={p} onClick={() => loadWordDetail(p.word)} />
                ))}
                {particles?.['2'].length === 0 && (
                  <p className="text-sm text-muted-foreground py-4 text-center">
                    No particles in this slot
                  </p>
                )}
              </div>
            </CardContent>
          </Card>

        </TabsContent>

        {/* USAGE GUIDE TAB */}
        <TabsContent value="usage" className="space-y-6">
          {/* Sentence Structure */}
          <Card>
            <CardHeader>
              <CardTitle>Basic Sentence Structure</CardTitle>
              <CardDescription>
                How particles fit into the Phi sentence
              </CardDescription>
            </CardHeader>
            <CardContent className="space-y-4">
              <div className="flex flex-wrap items-center gap-2 text-sm p-4 bg-muted rounded-lg">
                <Badge variant="outline">Slot 0</Badge>
                <span className="text-muted-foreground">→</span>
                <span className="font-medium">Subject</span>
                <span className="text-muted-foreground">→</span>
                <Badge variant="outline">Slot 1 (stacked)</Badge>
                <span className="text-muted-foreground">→</span>
                <Badge variant="outline">Slot 2</Badge>
                <span className="text-muted-foreground">→</span>
                <span className="font-medium">Content</span>
                <span className="text-muted-foreground">→</span>
                <span className="font-medium">Verb</span>
              </div>
              <p className="text-sm text-muted-foreground">
                Phi is a verb-final language. The verb comes at the end, preceded by all its modifiers
                and arguments. This allows the action to be fully contextualized before it is named.
              </p>
            </CardContent>
          </Card>

          {/* Slot 0 Usage */}
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <Badge>Slot 0</Badge>
                Framing the Sentence
              </CardTitle>
            </CardHeader>
            <CardContent className="space-y-6">
              <DocSection title="Questions with wa">
                <p>
                  The question particle <code>wa</code> transforms a statement into a gentle inquiry.
                  Its soft, open-sounding initial <em>w</em> is phonetically welcoming—an invitation
                  to share knowledge rather than a demand for answers.
                </p>
                <Example
                  phi="wa thi minu lothea"
                  gloss="Q 2SG family love"
                  translation="Do you love your family?"
                />
              </DocSection>

              <DocSection title="Requests with no">
                <p>
                  The imperative particle <code>no</code> frames utterances as cooperative requests
                  rather than commands. Its soft nasal sound is non-threatening, inviting the listener
                  into a shared purpose rather than imposing the speaker's will.
                </p>
                <Example
                  phi="no noshale shele"
                  gloss="IMP garden help"
                  translation="(Please) help the garden."
                />
              </DocSection>

              <DocSection title="Conditionals with lu">
                <p>
                  The conditional particle <code>lu</code> signals a shift into hypothetical thinking.
                  For unreal or counterfactual conditions, combine it with the irrealis marker <code>whe</code>.
                </p>
                <div className="space-y-3">
                  <Example
                    phi="lu thi shele, mia wela hisu"
                    gloss="COND 2SG help, 1SG good feel"
                    translation="If you help, I will feel good."
                  />
                  <Example
                    phi="lu whe mia to shele, shia ma to wepu"
                    gloss="COND IRR 1SG PST help, 3SG NEG PST leave"
                    translation="If I had helped [but I didn't], she would not have left."
                  />
                </div>
              </DocSection>

              <DocSection title="Wishes with su">
                <p>
                  The optative particle <code>su</code> frames sentences as hopes, wishes, or prayers.
                </p>
                <Example
                  phi="su weola wela nio"
                  gloss="OPT community good be"
                  translation="May the community be well."
                />
              </DocSection>

              <DocSection title="Politeness with pi">
                <p>
                  The politeness marker <code>pi</code> is a conscious declaration of social mindfulness.
                  It can combine with other Slot 0 particles.
                </p>
                <Example
                  phi="pi no minu shele"
                  gloss="POL IMP family help"
                  translation="Please help the family."
                />
              </DocSection>
            </CardContent>
          </Card>

          {/* Slot 1 Usage */}
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <Badge>Slot 1</Badge>
                Modifying the Action
              </CardTitle>
            </CardHeader>
            <CardContent className="space-y-6">
              <div className="p-4 bg-muted rounded-lg">
                <p className="text-sm font-medium mb-2">Stacking Order (when multiple particles appear):</p>
                <div className="flex flex-wrap gap-2 text-xs">
                  <Badge variant="outline">Tense</Badge>
                  <span>→</span>
                  <Badge variant="outline">Aspect</Badge>
                  <span>→</span>
                  <Badge variant="outline">Voice</Badge>
                  <span>→</span>
                  <Badge variant="outline">Evidentiality</Badge>
                  <span>→</span>
                  <Badge variant="outline">Modality</Badge>
                  <span>→</span>
                  <Badge variant="outline">Negation</Badge>
                </div>
              </div>

              <DocSection title="Tense: to (past) and so (future)">
                <p>
                  Present tense is unmarked—the default state of mindful presence. Past and future
                  require conscious temporal navigation.
                </p>
                <div className="space-y-3">
                  <Example
                    phi="mia kela"
                    gloss="1SG understand"
                    translation="I understand. (present, unmarked)"
                  />
                  <Example
                    phi="mia to kela"
                    gloss="1SG PST understand"
                    translation="I understood."
                  />
                  <Example
                    phi="mia so kela"
                    gloss="1SG FUT understand"
                    translation="I will understand."
                  />
                </div>
              </DocSection>

              <DocSection title="Aspect: The Internal Texture of Action">
                <p>
                  Aspect describes <em>how</em> an action unfolds, independent of when it occurs.
                </p>
                <div className="space-y-3">
                  <Example
                    phi="mia si kela"
                    gloss="1SG IPFV understand"
                    translation="I am understanding. (ongoing)"
                  />
                  <Example
                    phi="mia to ki kela"
                    gloss="1SG PST PFV understand"
                    translation="I have understood. (completed)"
                  />
                  <Example
                    phi="mia pa kela"
                    gloss="1SG INCH understand"
                    translation="I begin to understand."
                  />
                  <Example
                    phi="mia te kela"
                    gloss="1SG CESS understand"
                    translation="I stop understanding."
                  />
                </div>
              </DocSection>

              <DocSection title="Evidentiality: Epistemic Transparency">
                <p>
                  Evidential particles mark the <em>source</em> of the speaker's knowledge. Direct
                  experience is the unmarked default.
                </p>
                <div className="space-y-3">
                  <Example
                    phi="mia hi nila"
                    gloss="1SG DIR see"
                    translation="I see. (direct witness)"
                  />
                  <Example
                    phi="shia to ke wepu"
                    gloss="3SG PST INFER leave"
                    translation="She left. (I infer from evidence)"
                  />
                  <Example
                    phi="lo miona whi shele"
                    gloss="PL person REP help"
                    translation="People helped. (I was told)"
                  />
                  <Example
                    phi="thi ho kela"
                    gloss="2SG ASM understand"
                    translation="You understand. (I assume)"
                  />
                </div>
              </DocSection>

              <DocSection title="Modality: Possibility and Necessity">
                <div className="space-y-3">
                  <Example
                    phi="mia po kela"
                    gloss="1SG POSS understand"
                    translation="I can understand."
                  />
                  <Example
                    phi="mia na shele"
                    gloss="1SG NEC help"
                    translation="I must help."
                  />
                </div>
              </DocSection>

              <DocSection title="Voice: The Passive with se">
                <p>
                  The passive voice shifts focus from the agent to the patient of an action.
                </p>
                <div className="space-y-3">
                  <Example
                    phi="mia nophi kealo"
                    gloss="1SG story create"
                    translation="I create the story. (active)"
                  />
                  <Example
                    phi="nophi se kealo"
                    gloss="story PASS create"
                    translation="The story is created. (passive)"
                  />
                </div>
              </DocSection>

              <DocSection title="Causative: Making Things Happen">
                <p>
                  The causative particle <code>ka</code> indicates that the subject causes another
                  to perform the action.
                </p>
                <div className="space-y-3">
                  <Example
                    phi="pilo nima"
                    gloss="child sleep"
                    translation="The child sleeps."
                  />
                  <Example
                    phi="mia pilo ka nima"
                    gloss="1SG child CAUS sleep"
                    translation="I make the child sleep."
                  />
                </div>
              </DocSection>

              <DocSection title="Negation with ma">
                <p>
                  Negation always comes last in the Slot 1 stack, immediately before the verb.
                </p>
                <Example
                  phi="mia ma kela"
                  gloss="1SG NEG understand"
                  translation="I do not understand."
                />
              </DocSection>

              <DocSection title="Complex Stacking Example">
                <Example
                  phi="mia to si ke po ma kela"
                  gloss="1SG PST IPFV INFER POSS NEG understand"
                  translation="I was not being able to understand. (I infer)"
                />
              </DocSection>
            </CardContent>
          </Card>

          {/* Slot 2 Usage */}
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <Badge>Slot 2</Badge>
                Word-Level Modifications
              </CardTitle>
            </CardHeader>
            <CardContent className="space-y-6">
              <DocSection title="Plurality with lo">
                <p>
                  Use <code>lo</code> for unquantified plurals. When a number or quantifier is present,
                  plurality is already implied and <code>lo</code> is not needed.
                </p>
                <div className="space-y-3">
                  <Example
                    phi="lo whelea"
                    gloss="PL friend"
                    translation="friends (plural, unquantified)"
                  />
                  <Example
                    phi="wi whelea"
                    gloss="two friend"
                    translation="two friends (number implies plural)"
                  />
                </div>
              </DocSection>

              <DocSection title="Ordinals with nu">
                <Example
                  phi="nu ta pilo"
                  gloss="ORD one child"
                  translation="first child"
                />
              </DocSection>

              <DocSection title="Focus with she">
                <Example
                  phi="mia she lothea kela"
                  gloss="1SG FOC love understand"
                  translation="I understand *love* (specifically)"
                />
              </DocSection>

              <DocSection title="Comparison with mo">
                <div className="space-y-3">
                  <Example
                    phi="noshale sheo shiro mo wela nio"
                    gloss="garden than forest CMPR good be"
                    translation="The garden is more beautiful than the forest."
                  />
                  <Example
                    phi="pha noshale mo she wela nio"
                    gloss="PROX garden CMPR FOC good be"
                    translation="This garden is the most beautiful."
                  />
                </div>
              </DocSection>

              <DocSection title="Demonstratives: pha and tha">
                <div className="space-y-3">
                  <Example
                    phi="pha whelea"
                    gloss="PROX friend"
                    translation="this friend"
                  />
                  <Example
                    phi="tha whelea"
                    gloss="DIST friend"
                    translation="that friend"
                  />
                </div>
              </DocSection>

              <DocSection title="Honorifics: Social Relationships">
                <p>
                  Honorifics announce the speaker's relationship to a person before naming them.
                </p>
                <div className="space-y-3">
                  <Example
                    phi="sa Thala"
                    gloss="HON.RESPECT Thala"
                    translation="Honored Thala (mentor/elder)"
                  />
                  <Example
                    phi="ni Hino"
                    gloss="HON.INTIM Hino"
                    translation="Dear Hino (close friend/family)"
                  />
                  <Example
                    phi="le Mako"
                    gloss="HON.ROLE Mako"
                    translation="Respected Mako (community role)"
                  />
                </div>
              </DocSection>
            </CardContent>
          </Card>

          {/* Quick Reference */}
          <Card>
            <CardHeader>
              <CardTitle>Quick Reference</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="overflow-x-auto">
                <table className="w-full text-sm">
                  <thead>
                    <tr className="border-b">
                      <th className="text-left py-2 px-3">Slot</th>
                      <th className="text-left py-2 px-3">Function</th>
                      <th className="text-left py-2 px-3">Particles</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr className="border-b">
                      <td className="py-2 px-3"><Badge>0</Badge></td>
                      <td className="py-2 px-3">Sentence Frame</td>
                      <td className="py-2 px-3 font-mono">wa, no, lu, su, pi</td>
                    </tr>
                    <tr className="border-b">
                      <td className="py-2 px-3"><Badge>1</Badge></td>
                      <td className="py-2 px-3">Tense</td>
                      <td className="py-2 px-3 font-mono">to, so</td>
                    </tr>
                    <tr className="border-b">
                      <td className="py-2 px-3"></td>
                      <td className="py-2 px-3">Aspect</td>
                      <td className="py-2 px-3 font-mono">ki, si, pa, te</td>
                    </tr>
                    <tr className="border-b">
                      <td className="py-2 px-3"></td>
                      <td className="py-2 px-3">Voice</td>
                      <td className="py-2 px-3 font-mono">se</td>
                    </tr>
                    <tr className="border-b">
                      <td className="py-2 px-3"></td>
                      <td className="py-2 px-3">Evidentiality</td>
                      <td className="py-2 px-3 font-mono">hi, ke, whi, ho</td>
                    </tr>
                    <tr className="border-b">
                      <td className="py-2 px-3"></td>
                      <td className="py-2 px-3">Modality</td>
                      <td className="py-2 px-3 font-mono">po, na, ka</td>
                    </tr>
                    <tr className="border-b">
                      <td className="py-2 px-3"></td>
                      <td className="py-2 px-3">Negation</td>
                      <td className="py-2 px-3 font-mono">ma</td>
                    </tr>
                    <tr>
                      <td className="py-2 px-3"><Badge>2</Badge></td>
                      <td className="py-2 px-3">Word-Level</td>
                      <td className="py-2 px-3 font-mono">lo, nu, she, mo, pha, tha, sa, ni, le</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </CardContent>
          </Card>
        </TabsContent>
      </Tabs>

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
              <div className="flex gap-2">
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

                <div className="flex gap-6">
                  <div>
                    <h4 className="text-xs uppercase tracking-wider text-muted-foreground mb-1">
                      Slot
                    </h4>
                    <Badge>{selectedWord.slot !== null ? `Slot ${selectedWord.slot}` : 'N/A'}</Badge>
                  </div>
                  <div>
                    <h4 className="text-xs uppercase tracking-wider text-muted-foreground mb-1">
                      Category
                    </h4>
                    <Badge variant="outline">{selectedWord.subcategory || selectedWord.category}</Badge>
                  </div>
                </div>

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
                />

                {(displayGrammaticalNotes || editing) && (
                  <EditableField
                    label="Grammatical Notes"
                    value={displayGrammaticalNotes || undefined}
                    editing={editing}
                    onChange={(v) => updateEditField('grammatical_notes', v)}
                    multiline
                  />
                )}

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
                    {!editing && Object.values(displayPillars).filter(Boolean).length === 0 && (
                      <p className="text-sm text-muted-foreground/50">No pillars defined</p>
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
