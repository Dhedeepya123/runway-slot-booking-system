import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export const getBookings = async () => {
  return await axios.get(`${API_URL}/bookings/`);
};

export const createBooking = async (bookingData) => {
  return await axios.post(`${API_URL}/bookings/`, bookingData);
};

export const approveBooking = async (id) => {
  return await axios.put(`${API_URL}/bookings/${id}/approve`);
};

export const rejectBooking = async (id) => {
  return await axios.put(`${API_URL}/bookings/${id}/reject`);
};

export const deleteBooking = async (id) => {
  return await axios.delete(`${API_URL}/bookings/${id}`);
};