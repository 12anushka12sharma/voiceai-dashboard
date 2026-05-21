import React, { useState } from 'react';
import axios from 'axios';
import { useDashboardStore } from '../store';

const Upload: React.FC = () => {
  const [isDragging, setIsDragging] = useState(false);
  const [uploading, setUploading] = useState(false);
  const { importHistory, setImportHistory } = useDashboardStore();

  const handleDragOver = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(true);
  };

  const handleDragLeave = () => {
    setIsDragging(false);
  };

  const handleDrop = async (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(false);
    
    const files = e.dataTransfer.files;
    if (files.length > 0) {
      await uploadFile(files[0]);
    }
  };

  const uploadFile = async (file: File) => {
    if (\!file.name.endsWith('.csv')) {
      alert('Please upload a CSV file');
      return;
    }

    setUploading(true);
    try {
      const formData = new FormData();
      formData.append('file', file);

      const response = await axios.post(
        'http://localhost:8000/api/upload',
        formData,
        { headers: { 'Content-Type': 'multipart/form-data' } }
      );

      // Refresh history
      const historyResponse = await axios.get('http://localhost:8000/api/history');
      setImportHistory(historyResponse.data.data);

      alert(`Upload successful\! Processing ${response.data.total_calls} calls...`);
    } catch (error) {
      console.error('Upload error:', error);
      alert('Upload failed. Please try again.');
    } finally {
      setUploading(false);
    }
  };

  return (
    <div className="space-y-8">
      {/* Upload Area */}
      <div
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        onDrop={handleDrop}
        className={`border-2 border-dashed rounded-lg p-12 text-center transition-colors ${
          isDragging
            ? 'border-blue-500 bg-blue-50'
            : 'border-gray-300 bg-gray-50'
        }`}
      >
        <div className="text-5xl mb-4">📤</div>
        <h3 className="text-xl font-semibold text-gray-900 mb-2">
          Drop your CSV file here
        </h3>
        <p className="text-gray-600 mb-4">or</p>
        <label className="inline-block">
          <input
            type="file"
            accept=".csv"
            onChange={(e) => e.target.files && uploadFile(e.target.files[0])}
            className="hidden"
            disabled={uploading}
          />
          <span className="px-6 py-2 bg-blue-600 text-white rounded-lg cursor-pointer hover:bg-blue-700 inline-block">
            {uploading ? 'Uploading...' : 'Select File'}
          </span>
        </label>
      </div>

      {/* Recent Uploads */}
      <div className="bg-white rounded-lg shadow overflow-hidden">
        <div className="px-6 py-4 border-b border-gray-200">
          <h3 className="text-lg font-semibold">Recent Imports</h3>
        </div>
        <div className="overflow-x-auto">
          <table className="w-full">
            <thead className="bg-gray-50 border-b border-gray-200">
              <tr>
                <th className="px-6 py-3 text-left text-sm font-semibold text-gray-900">File</th>
                <th className="px-6 py-3 text-left text-sm font-semibold text-gray-900">Calls</th>
                <th className="px-6 py-3 text-left text-sm font-semibold text-gray-900">Status</th>
                <th className="px-6 py-3 text-left text-sm font-semibold text-gray-900">Date</th>
              </tr>
            </thead>
            <tbody>
              {importHistory.map((imp: any) => (
                <tr key={imp.id} className="border-b border-gray-200 hover:bg-gray-50">
                  <td className="px-6 py-4 text-sm text-gray-900">{imp.filename}</td>
                  <td className="px-6 py-4 text-sm text-gray-600">{imp.total_calls}</td>
                  <td className="px-6 py-4 text-sm">
                    <span className={`px-3 py-1 rounded-full text-xs font-semibold ${
                      imp.status === 'completed' ? 'bg-green-100 text-green-800' :
                      imp.status === 'processing' ? 'bg-blue-100 text-blue-800' :
                      'bg-red-100 text-red-800'
                    }`}>
                      {imp.status}
                    </span>
                  </td>
                  <td className="px-6 py-4 text-sm text-gray-600">
                    {new Date(imp.upload_date).toLocaleDateString()}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default Upload;
