import "./Footer.css";
import {
  FaInstagram,
  FaTiktok,
  FaEnvelope,
  FaMusic,
} from "react-icons/fa";
import { motion } from "framer-motion";
import React from "react";

const Footer: React.FC = () => {
  const socialLinks = [
    {
      icon: <FaMusic />,
      url: "https://link.ghostpavilion.com/no-way-to-love",
      label: "Toneden"
    },
    {
      icon: <FaInstagram />,
      url: "https://www.instagram.com/ghost_pavilion",
      label: "Instagram"
    },
    {
      icon: <FaTiktok />,
      url: "https://www.tiktok.com/@ghostpavilion",
      label: "TikTok"
    },
    {
      icon: <FaEnvelope />,
      url: "mailto:info@ghostpavilion.com",
      label: "Email"
    },
  ];

  return (
    <section className="footer">
      <ul className="links">
        {socialLinks.map(({ icon, url }, index) => (
          <li key={index}>
            <a href={url} target="_blank" rel="noopener noreferrer">
              <motion.div
                whileHover={{ scale: 1.3 }}
                transition={{ type: "spring", stiffness: 300 }}
              >
                {React.cloneElement(icon, { className: "icons" })}
              </motion.div>
            </a>
          </li>
        ))}
      </ul>
    </section>
  );
};

export default Footer;
