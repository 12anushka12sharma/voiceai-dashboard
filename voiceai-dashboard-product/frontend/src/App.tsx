import React, { useEffect } from 'react';
import { useDashboardStore } from './store';
import Dashboard from './components/Dashboard';
import Upload from './components/Upload';
import Filters from './components/Filters';
import { fetchMetrics, fetchIssues, fetchSentimentTrends } from './api';
import axios from 'axios';

const App: React.FC = () => {
  const { selectedTab, setSelectedTab, setImportHistory } = useDashboardStore();

  useEffect(() => {
    const loadHistory = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/history');
        setImportHistory(response.data.data);
      } catch (error) {
        console.error('Error loading import history:', error);
      }
    };

    loadHistory();
  }, []);

  return (
    <div className="min-h-screen bg-gray-100">
      {/* Header */}
      <header className="bg-white shadow">
        <div className="max-w-7xl mx-auto px-4 py-6">
          <h1 className="text-3xl font-bold text-gray-900">
            🎤 VoiceAI Call Analysis Dashboard
          </h1>
          <p className="text-gray-600 mt-2">
            Real-time sentiment analysis and performance metrics
          </p>
        </div>
      </header>

      {/* Navigation */}
      <div className="bg-white border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-4">
          <div className="flex gap-8">
            <button
              onClick={() => setSelectedTab('dashboard')}
              className={`py-4 px-2 font-medium border-b-2 ${
                selectedTab === 'dashboard'
                  ? 'text-blue-600 border-blue-600'
                  : 'text-gray-600 border-transparent hover:text-gray-900'
              }`}
            >
              📊 Dashboard
            </button>
            <button
              onClick={() => setSelectedTab('upload')}
              className={`py-4 px-2 font-medium border-b-2 ${
                selectedTab === 'upload'
                  ? 'text-blue-600 border-blue-600'
                  : 'text-gray-600 border-transparent hover:text-gray-900'
              }`}
            >
              📤 Upload Data
            </button>
            <button
              onClick={() => setSelectedTab('data')}
              className={`py-4 px-2 font-medium border-b-2 ${
                selectedTab === 'data'
                  ? 'text-blue-600 border-blue-600'
                  : 'text-gray-600 border-transparent hover:text-gray-900'
              }`}
            >
              📋 Raw Data
            </button>
          </div>
        </div>
      </div>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 py-8">
        {selectedTab === 'dashboard' && (
          <div className="space-y-6">
            <Filters />
            <Dashboard />
          </div>
        )}

        {selectedTab === 'upload' && <Upload />}

        {selectedTab === 'data' && (
          <div className="bg-white rounded-lg shadow p-6">
            <h2 className="text-xl font-semibold mb-4">Call Data Explorer</h2>
            <p className="text-gray-600">Coming soon...</p>
          </div>
        )}
      </main>

      {/* Footer */}
      <footer className="bg-white border-t border-gray-200 mt-12">
        <div className="max-w-7xl mx-auto px-4 py-6 text-center text-gray-600 text-sm">
          <p>VoiceAI Call Analysis • Powered by voiceai_call_analysis skill</p>
        </div>
      </footer>
    </div>
  );
};

export default App;
