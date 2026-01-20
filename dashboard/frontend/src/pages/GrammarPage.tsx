import { useState, useEffect } from 'react'
import { FileText } from 'lucide-react'
import { ScrollArea } from '@/components/ui/scroll-area'
import { Button } from '@/components/ui/button'
import { Separator } from '@/components/ui/separator'
import { api, type GrammarDoc, type GrammarContent } from '@/lib/utils'
import { cn } from '@/lib/utils'

export default function GrammarPage() {
  const [docs, setDocs] = useState<GrammarDoc[]>([])
  const [selectedPath, setSelectedPath] = useState<string | null>(null)
  const [content, setContent] = useState<GrammarContent | null>(null)
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    loadDocs()
  }, [])

  const loadDocs = async () => {
    try {
      const data = await api<GrammarDoc[]>('/grammar')
      setDocs(data)
    } catch (e) {
      console.error('Failed to load grammar docs:', e)
    }
  }

  const loadContent = async (path: string) => {
    setLoading(true)
    setSelectedPath(path)
    try {
      const data = await api<GrammarContent>(`/grammar/${path}`)
      setContent(data)
    } catch (e) {
      console.error('Failed to load grammar content:', e)
    }
    setLoading(false)
  }

  // Separate grammar docs from other docs
  const grammarDocs = docs.filter((d) => d.path.startsWith('grammar/'))
  const otherDocs = docs.filter((d) => !d.path.startsWith('grammar/'))

  return (
    <div className="flex h-full">
      {/* Sidebar */}
      <aside className="w-64 border-r bg-card">
        <div className="p-4">
          <h3 className="font-medium text-sm text-muted-foreground uppercase tracking-wider">
            Grammar
          </h3>
        </div>
        <ScrollArea className="h-[calc(100vh-180px)]">
          <div className="px-2 space-y-1">
            {grammarDocs.map((doc) => (
              <Button
                key={doc.path}
                variant="ghost"
                size="sm"
                className={cn(
                  'w-full justify-start text-sm',
                  selectedPath === doc.path && 'bg-primary/10 text-primary'
                )}
                onClick={() => loadContent(doc.path)}
              >
                <FileText className="h-4 w-4 mr-2 flex-shrink-0" />
                <span className="truncate">{doc.title}</span>
              </Button>
            ))}
          </div>

          {otherDocs.length > 0 && (
            <>
              <Separator className="my-4" />
              <div className="px-4 pb-2">
                <h3 className="font-medium text-sm text-muted-foreground uppercase tracking-wider">
                  Guides
                </h3>
              </div>
              <div className="px-2 space-y-1">
                {otherDocs.map((doc) => (
                  <Button
                    key={doc.path}
                    variant="ghost"
                    size="sm"
                    className={cn(
                      'w-full justify-start text-sm',
                      selectedPath === doc.path && 'bg-primary/10 text-primary'
                    )}
                    onClick={() => loadContent(doc.path)}
                  >
                    <FileText className="h-4 w-4 mr-2 flex-shrink-0" />
                    <span className="truncate">{doc.title}</span>
                  </Button>
                ))}
              </div>
            </>
          )}
        </ScrollArea>
      </aside>

      {/* Content */}
      <main className="flex-1 overflow-hidden">
        {loading ? (
          <div className="flex items-center justify-center h-full text-muted-foreground">
            Loading...
          </div>
        ) : content ? (
          <ScrollArea className="h-full">
            <article className="p-8 max-w-4xl">
              <h1 className="text-3xl font-light text-primary mb-8">
                {content.title}
              </h1>
              <div
                className="prose prose-neutral dark:prose-invert max-w-none"
                dangerouslySetInnerHTML={{ __html: content.content }}
              />
            </article>
          </ScrollArea>
        ) : (
          <div className="flex flex-col items-center justify-center h-full text-muted-foreground">
            <FileText className="h-12 w-12 mb-4 opacity-20" />
            <p>Select a document from the sidebar to view</p>
          </div>
        )}
      </main>
    </div>
  )
}
