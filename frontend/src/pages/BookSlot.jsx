import { useState } from "react";
import { createBooking } from "../api/bookings";
import Navbar from "../components/Navbar";

export default function BookSlot() {
  const [formData, setFormData] = useState({
    flight_number: "",
    airline: "",
    runway: "",
    date: "",
    start_time: "",
    end_time: "",
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await createBooking(formData);

      if (response.data.message === "Conflict detected") {
        alert(
          `Conflict detected!\nSuggested Slot:\n${response.data.suggested_slot.start_time} - ${response.data.suggested_slot.end_time}`
        );
      } else {
        alert("Booking created successfully!");

        setFormData({
          flight_number: "",
          airline: "",
          runway: "",
          date: "",
          start_time: "",
          end_time: "",
        });
      }
    } catch (error) {
      alert("Failed to create booking.");
      console.error(error);
    }
  };

  return (
    <>
      <Navbar />

      <div style={{ padding: "20px" }}>
        <h2>Book Runway Slot</h2>

        <form onSubmit={handleSubmit}>
          <input
            type="text"
            name="flight_number"
            placeholder="Flight Number"
            value={formData.flight_number}
            onChange={handleChange}
          />
          <br /><br />

          <input
            type="text"
            name="airline"
            placeholder="Airline"
            value={formData.airline}
            onChange={handleChange}
          />
          <br /><br />

          <input
            type="text"
            name="runway"
            placeholder="Runway"
            value={formData.runway}
            onChange={handleChange}
          />
          <br /><br />

          <input
            type="date"
            name="date"
            value={formData.date}
            onChange={handleChange}
          />
          <br /><br />

          <input
            type="time"
            name="start_time"
            value={formData.start_time}
            onChange={handleChange}
          />
          <br /><br />

          <input
            type="time"
            name="end_time"
            value={formData.end_time}
            onChange={handleChange}
          />
          <br /><br />

          <button type="submit">Book Slot</button>
        </form>
      </div>
    </>
  );
}