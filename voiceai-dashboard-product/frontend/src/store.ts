import { create } from 'zustand';

interface Filters {
  startDate: string | null;
  endDate: string | null;
  sentiment: string | null;
  issueCategory: string | null;
  csatMin: number | null;
  csatMax: number | null;
}

interface DashboardStore {
  metrics: any;
  callData: any[];
  issueBreakdown: any;
  sentimentTrends: any;
  importHistory: any[];
  filters: Filters;
  loading: boolean;
  selectedTab: string;
  
  setMetrics: (metrics: any) => void;
  setCallData: (data: any[]) => void;
  setIssueBreakdown: (data: any) => void;
  setSentimentTrends: (data: any) => void;
  setImportHistory: (data: any[]) => void;
  setFilters: (filters: Partial<Filters>) => void;
  clearFilters: () => void;
  setLoading: (loading: boolean) => void;
  setSelectedTab: (tab: string) => void;
}

const initialFilters: Filters = {
  startDate: null,
  endDate: null,
  sentiment: null,
  issueCategory: null,
  csatMin: null,
  csatMax: null,
};

export const useDashboardStore = create<DashboardStore>((set) => ({
  metrics: null,
  callData: [],
  issueBreakdown: {},
  sentimentTrends: {},
  importHistory: [],
  filters: initialFilters,
  loading: false,
  selectedTab: 'dashboard',
  
  setMetrics: (metrics) => set({ metrics }),
  setCallData: (data) => set({ callData: data }),
  setIssueBreakdown: (data) => set({ issueBreakdown: data }),
  setSentimentTrends: (data) => set({ sentimentTrends: data }),
  setImportHistory: (data) => set({ importHistory: data }),
  setFilters: (filters) => set((state) => ({ 
    filters: { ...state.filters, ...filters } 
  })),
  clearFilters: () => set({ filters: initialFilters }),
  setLoading: (loading) => set({ loading }),
  setSelectedTab: (tab) => set({ selectedTab: tab }),
}));
