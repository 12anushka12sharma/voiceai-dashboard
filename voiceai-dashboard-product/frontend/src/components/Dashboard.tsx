import React, { useEffect } from 'react';
import {
  BarChart, Bar, LineChart, Line, PieChart, Pie, Cell,
  XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer
} from 'recharts';
import { useDashboardStore } from '../store';
import { fetchMetrics, fetchIssues, fetchSentimentTrends } from '../api';

const Dashboard: React.FC = () => {
  const { metrics, issueBreakdown, sentimentTrends, filters, setMetrics, setIssueBreakdown, setSentimentTrends, setLoading } = useDashboardStore();

  useEffect(() => {
    const loadData = async () => {
      setLoading(true);
      try {
        const metricsData = await fetchMetrics(filters);
        const issuesData = await fetchIssues(filters);
        const sentimentData = await fetchSentimentTrends(filters);
        
        setMetrics(metricsData);
        setIssueBreakdown(issuesData);
        setSentimentTrends(sentimentData);
      } catch (error) {
        console.error('Error loading data:', error);
      } finally {
        setLoading(false);
      }
    };

    loadData();
  }, [filters]);

  if (\!metrics) return <div className="p-8">Loading...</div>;

  const COLORS = ['#ef4444', '#f59e0b', '#10b981', '#3b82f6'];

  return (
    <div className="space-y-8">
      {/* KPI Cards */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <KPICard 
          title="Total Calls" 
          value={metrics.total_calls} 
          icon="📞"
        />
        <KPICard 
          title="Negative Sentiment" 
          value={`${metrics.negative_sentiment_pct}%`}
          icon="😞"
          bgColor="bg-red-50"
        />
        <KPICard 
          title="Avg CSAT" 
          value={`${metrics.avg_csat}/5`}
          icon="⭐"
          bgColor="bg-blue-50"
        />
        <KPICard 
          title="Resolution Rate" 
          value={`${metrics.resolution_rate_pct}%`}
          icon="✓"
          bgColor="bg-green-50"
        />
      </div>

      {/* Charts */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        
        {/* Sentiment Distribution */}
        <div className="bg-white p-6 rounded-lg shadow">
          <h3 className="text-lg font-semibold mb-4">Sentiment Distribution</h3>
          <ResponsiveContainer width="100%" height={300}>
            <PieChart>
              <Pie
                data={[
                  { name: 'Positive', value: metrics.positive_sentiment_pct },
                  { name: 'Neutral', value: metrics.neutral_sentiment_pct },
                  { name: 'Negative', value: metrics.negative_sentiment_pct }
                ]}
                cx="50%"
                cy="50%"
                labelLine={false}
                label={({ name, value }) => `${name}: ${value}%`}
                outerRadius={80}
                fill="#8884d8"
                dataKey="value"
              >
                <Cell fill="#10b981" />
                <Cell fill="#6b7280" />
                <Cell fill="#ef4444" />
              </Pie>
            </PieChart>
          </ResponsiveContainer>
        </div>

        {/* Top Issues */}
        <div className="bg-white p-6 rounded-lg shadow">
          <h3 className="text-lg font-semibold mb-4">Top Issues by Negative Sentiment</h3>
          <ResponsiveContainer width="100%" height={300}>
            <BarChart
              data={Object.entries(issueBreakdown)
                .map(([name, data]: any) => ({ name, negative_pct: data.negative_pct }))
                .sort((a: any, b: any) => b.negative_pct - a.negative_pct)
                .slice(0, 5)}
            >
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" angle={-45} textAnchor="end" height={80} />
              <YAxis />
              <Tooltip />
              <Bar dataKey="negative_pct" fill="#ef4444" />
            </BarChart>
          </ResponsiveContainer>
        </div>

        {/* Sentiment Trends */}
        <div className="bg-white p-6 rounded-lg shadow lg:col-span-2">
          <h3 className="text-lg font-semibold mb-4">Sentiment Trends Over Time</h3>
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={Object.entries(sentimentTrends).map(([date, data]: any) => ({
              date,
              ...data
            }))}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="date" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Line type="monotone" dataKey="positive_pct" stroke="#10b981" name="Positive %" />
              <Line type="monotone" dataKey="negative_pct" stroke="#ef4444" name="Negative %" />
              <Line type="monotone" dataKey="neutral_pct" stroke="#6b7280" name="Neutral %" />
            </LineChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
};

interface KPICardProps {
  title: string;
  value: string | number;
  icon: string;
  bgColor?: string;
}

const KPICard: React.FC<KPICardProps> = ({ title, value, icon, bgColor = 'bg-blue-50' }) => (
  <div className={`${bgColor} p-6 rounded-lg border border-gray-200`}>
    <div className="text-3xl mb-2">{icon}</div>
    <p className="text-gray-600 text-sm">{title}</p>
    <p className="text-2xl font-bold text-gray-900">{value}</p>
  </div>
);

export default Dashboard;
