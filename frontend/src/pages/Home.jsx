import Navbar from "../components/Navbar";

export default function Home() {
  return (
    <>
      <Navbar />

      <div style={{ padding: "20px" }}>
        <h1>Runway Slot Booking System</h1>

        <p>
          Welcome to the Runway Slot Booking System built using React and
          FastAPI.
        </p>

        <h3>Features</h3>

        <ul>
          <li>Book runway slots for flights</li>
          <li>Automatic conflict detection</li>
          <li>Suggested next available slot</li>
          <li>Admin approval and rejection</li>
          <li>View all bookings</li>
        </ul>
      </div>
    </>
  );
}