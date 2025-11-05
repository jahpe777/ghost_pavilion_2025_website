import { useState } from "react";
import axios from "axios";
import "./SignUpPage.css";

const SignUpPage = () => {
  const [formData, setFormData] = useState({ name: "", email: "" });
  const [success, setSuccess] = useState(false);
  const [error, setError] = useState("");

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        "https://ghostpavilion2025-production.up.railway.app/api/signup/",
        formData
      );
      if (response.status === 201) {
        setSuccess(true);
        setError("");
        setFormData({ name: "", email: "" });
      }
    } catch (err: any) {
      console.error(err);
      setError("Failed to sign up. Please try again.");
    }
  };

  return (
    <section className="signup-page">
      <h2>Join the Ghost Pavilion Mailing List</h2>
      <p className="signup-subtext">
        Get notified about exclusive content, merch, and event drops
      </p>
      {success && <p className="success-msg">Thank you for signing up!</p>}
      {error && <p className="error-msg">{error}</p>}
      <form onSubmit={handleSubmit}>
        <input
          name="name"
          placeholder="Your Name"
          value={formData.name}
          onChange={handleChange}
          required
        />
        <input
          name="email"
          type="email"
          placeholder="Your Email"
          value={formData.email}
          onChange={handleChange}
          required
        />
        <button type="submit">Sign Up</button>
      </form>
    </section>
  );
};

export default SignUpPage;
