import { useState, useEffect } from 'react'
import { Routes, Route, NavLink } from 'react-router-dom'
import { Book, FileText, Plus, RefreshCw, Layers } from 'lucide-react'
import { Button } from '@/components/ui/button'
import { Separator } from '@/components/ui/separator'
import { ThemeProvider } from '@/components/theme-provider'
import { ThemeToggle } from '@/components/theme-toggle'
import { api, type Stats } from '@/lib/utils'
import VocabularyPage from '@/pages/VocabularyPage'
import ParticlesPage from '@/pages/ParticlesPage'
import GrammarPage from '@/pages/GrammarPage'
import CreateWordPage from '@/pages/CreateWordPage'

function App() {
  const [stats, setStats] = useState<Stats | null>(null)
  const [syncing, setSyncing] = useState(false)

  useEffect(() => {
    loadStats()
  }, [])

  const loadStats = async () => {
    try {
      const data = await api<Stats>('/stats')
      setStats(data)
    } catch (e) {
      console.error('Failed to load stats:', e)
    }
  }

  const handleSync = async () => {
    setSyncing(true)
    try {
      await api('/sync', { method: 'POST' })
      await loadStats()
    } catch (e) {
      console.error('Sync failed:', e)
    }
    setSyncing(false)
  }

  return (
    <ThemeProvider defaultTheme="dark" storageKey="phi-ui-theme">
    <div className="flex h-screen bg-background">
      {/* Sidebar */}
      <aside className="w-64 border-r bg-card flex flex-col">
        <div className="p-6 flex items-start justify-between">
          <div>
            <h1 className="text-2xl font-light tracking-wide text-primary">Phi</h1>
            <p className="text-xs text-muted-foreground uppercase tracking-wider mt-1">
              Language Dashboard
            </p>
          </div>
          <ThemeToggle />
        </div>

        <Separator />

        <nav className="flex-1 p-4 space-y-1">
          <NavLink
            to="/"
            className={({ isActive }) =>
              `flex items-center gap-3 px-3 py-2 rounded-md text-sm transition-colors ${
                isActive
                  ? 'bg-primary/10 text-primary font-medium'
                  : 'text-muted-foreground hover:bg-muted hover:text-foreground'
              }`
            }
          >
            <Book className="h-4 w-4" />
            Vocabulary
          </NavLink>

          <NavLink
            to="/particles"
            className={({ isActive }) =>
              `flex items-center gap-3 px-3 py-2 rounded-md text-sm transition-colors ${
                isActive
                  ? 'bg-primary/10 text-primary font-medium'
                  : 'text-muted-foreground hover:bg-muted hover:text-foreground'
              }`
            }
          >
            <Layers className="h-4 w-4" />
            Particles
          </NavLink>

          <NavLink
            to="/grammar"
            className={({ isActive }) =>
              `flex items-center gap-3 px-3 py-2 rounded-md text-sm transition-colors ${
                isActive
                  ? 'bg-primary/10 text-primary font-medium'
                  : 'text-muted-foreground hover:bg-muted hover:text-foreground'
              }`
            }
          >
            <FileText className="h-4 w-4" />
            Grammar
          </NavLink>

          <NavLink
            to="/create"
            className={({ isActive }) =>
              `flex items-center gap-3 px-3 py-2 rounded-md text-sm transition-colors ${
                isActive
                  ? 'bg-primary/10 text-primary font-medium'
                  : 'text-muted-foreground hover:bg-muted hover:text-foreground'
              }`
            }
          >
            <Plus className="h-4 w-4" />
            Create Word
          </NavLink>
        </nav>

        <Separator />

        {/* Stats */}
        <div className="p-4">
          <div className="text-center mb-4">
            <div className="text-3xl font-light text-primary">
              {stats?.total ?? '—'}
            </div>
            <div className="text-xs text-muted-foreground uppercase tracking-wider">
              Total Words
            </div>
          </div>

          {stats && (
            <div className="grid grid-cols-3 gap-2 text-center text-xs">
              <div>
                <div className="font-medium">{stats.by_category.content || 0}</div>
                <div className="text-muted-foreground">Content</div>
              </div>
              <div>
                <div className="font-medium">{stats.by_category.function || 0}</div>
                <div className="text-muted-foreground">Function</div>
              </div>
              <div>
                <div className="font-medium">{stats.by_category.interjection || 0}</div>
                <div className="text-muted-foreground">Interj.</div>
              </div>
            </div>
          )}
        </div>

        <div className="p-4 pt-0">
          <Button
            variant="outline"
            size="sm"
            className="w-full"
            onClick={handleSync}
            disabled={syncing}
          >
            <RefreshCw className={`h-4 w-4 mr-2 ${syncing ? 'animate-spin' : ''}`} />
            {syncing ? 'Syncing...' : 'Sync Database'}
          </Button>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 overflow-auto">
        <Routes>
          <Route path="/" element={<VocabularyPage />} />
          <Route path="/particles" element={<ParticlesPage />} />
          <Route path="/grammar" element={<GrammarPage />} />
          <Route path="/create" element={<CreateWordPage />} />
        </Routes>
      </main>
    </div>
    </ThemeProvider>
  )
}

export default App
