import React from 'react';
import { useDashboardStore } from '../store';

const Filters: React.FC = () => {
  const { filters, setFilters, clearFilters } = useDashboardStore();

  return (
    <div className="bg-white rounded-lg shadow p-6">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-semibold">Filters</h3>
        <button
          onClick={() => clearFilters()}
          className="text-sm text-blue-600 hover:text-blue-700 font-medium"
        >
          Clear All
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        {/* Date Range */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            Start Date
          </label>
          <input
            type="date"
            value={filters.startDate || ''}
            onChange={(e) => setFilters({ startDate: e.target.value || null })}
            className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            End Date
          </label>
          <input
            type="date"
            value={filters.endDate || ''}
            onChange={(e) => setFilters({ endDate: e.target.value || null })}
            className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>

        {/* Sentiment */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            Sentiment
          </label>
          <select
            value={filters.sentiment || ''}
            onChange={(e) => setFilters({ sentiment: e.target.value || null })}
            className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            <option value="">All Sentiments</option>
            <option value="Positive">Positive</option>
            <option value="Neutral">Neutral</option>
            <option value="Negative">Negative</option>
          </select>
        </div>

        {/* CSAT Range */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            CSAT Score
          </label>
          <select
            onChange={(e) => {
              if (e.target.value === 'all') {
                setFilters({ csatMin: null, csatMax: null });
              } else if (e.target.value === '45') {
                setFilters({ csatMin: 4, csatMax: 5 });
              } else if (e.target.value === '3') {
                setFilters({ csatMin: 3, csatMax: 3 });
              } else if (e.target.value === '12') {
                setFilters({ csatMin: 1, csatMax: 2 });
              }
            }}
            className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            <option value="all">All Scores</option>
            <option value="45">4-5 (Satisfied)</option>
            <option value="3">3 (Neutral)</option>
            <option value="12">1-2 (Dissatisfied)</option>
          </select>
        </div>
      </div>

      <div className="mt-4 p-3 bg-blue-50 rounded-lg text-sm text-blue-700">
        💡 Filters are applied in real-time. Adjust them to explore different segments of your data.
      </div>
    </div>
  );
};

export default Filters;
