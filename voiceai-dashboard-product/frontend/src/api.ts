import axios from 'axios';

const API_BASE = 'http://localhost:8000/api';

export const fetchMetrics = async (filters: any) => {
  const params = new URLSearchParams();
  if (filters.startDate) params.append('start_date', filters.startDate);
  if (filters.endDate) params.append('end_date', filters.endDate);
  if (filters.sentiment) params.append('sentiment', filters.sentiment);
  if (filters.issueCategory) params.append('issue_category', filters.issueCategory);

  const response = await axios.get(`${API_BASE}/metrics?${params}`);
  return response.data;
};

export const fetchCallData = async (filters: any, skip = 0, limit = 100) => {
  const params = new URLSearchParams();
  params.append('skip', skip.toString());
  params.append('limit', limit.toString());
  
  if (filters.startDate) params.append('start_date', filters.startDate);
  if (filters.endDate) params.append('end_date', filters.endDate);
  if (filters.sentiment) params.append('sentiment', filters.sentiment);
  if (filters.issueCategory) params.append('issue_category', filters.issueCategory);
  if (filters.csatMin) params.append('csat_min', filters.csatMin.toString());
  if (filters.csatMax) params.append('csat_max', filters.csatMax.toString());

  const response = await axios.get(`${API_BASE}/data?${params}`);
  return response.data;
};

export const fetchIssues = async (filters: any) => {
  const params = new URLSearchParams();
  if (filters.startDate) params.append('start_date', filters.startDate);
  if (filters.endDate) params.append('end_date', filters.endDate);

  const response = await axios.get(`${API_BASE}/issues?${params}`);
  return response.data;
};

export const fetchSentimentTrends = async (filters: any) => {
  const params = new URLSearchParams();
  params.append('period', 'daily');
  if (filters.startDate) params.append('start_date', filters.startDate);
  if (filters.endDate) params.append('end_date', filters.endDate);

  const response = await axios.get(`${API_BASE}/sentiment?${params}`);
  return response.data;
};

export const exportExcel = async (importId: number) => {
  window.location.href = `${API_BASE}/export/excel/${importId}`;
};
