import { useEffect, useState } from "react";
import {
  getBookings,
  approveBooking,
  rejectBooking,
  deleteBooking,
} from "../api/bookings";
import Navbar from "../components/Navbar";

export default function Admin() {
  const [bookings, setBookings] = useState([]);

  const loadBookings = async () => {
    try {
      const response = await getBookings();
      setBookings(response.data);
    } catch (error) {
      console.error("Error fetching bookings:", error);
    }
  };

  useEffect(() => {
    loadBookings();
  }, []);

  const handleApprove = async (id) => {
    await approveBooking(id);
    loadBookings();
  };

  const handleReject = async (id) => {
    await rejectBooking(id);
    loadBookings();
  };

  const handleDelete = async (id) => {
    await deleteBooking(id);
    loadBookings();
  };

  return (
    <>
      <Navbar />

      <div style={{ padding: "20px" }}>
        <h2>Admin Dashboard</h2>

        <table border="1" cellPadding="8" style={{ borderCollapse: "collapse", width: "100%" }}>
          <thead>
            <tr>
              <th>ID</th>
              <th>Flight</th>
              <th>Airline</th>
              <th>Runway</th>
              <th>Date</th>
              <th>Start</th>
              <th>End</th>
              <th>Status</th>
              <th>Actions</th>
            </tr>
          </thead>

          <tbody>
            {bookings.map((booking) => (
              <tr key={booking.id}>
                <td>{booking.id}</td>
                <td>{booking.flight_number}</td>
                <td>{booking.airline}</td>
                <td>{booking.runway}</td>
                <td>{booking.date}</td>
                <td>{booking.start_time}</td>
                <td>{booking.end_time}</td>
                <td>{booking.status}</td>

                <td>
                  <button onClick={() => handleApprove(booking.id)}>
                    Approve
                  </button>

                  {" "}

                  <button onClick={() => handleReject(booking.id)}>
                    Reject
                  </button>

                  {" "}

                  <button onClick={() => handleDelete(booking.id)}>
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </>
  );
}