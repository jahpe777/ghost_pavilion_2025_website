import { motion } from "framer-motion";
import "./EPKPage.css";

import albumArt from "../Images/Frame_26.png";
import pressPhoto1 from "../Images/GhostPavilion1byLaurenChang.JPG";
import pressPhoto2 from "../Images/GhostPavilion2byLaurenChang.JPG";

const EPKPage = () => {
  return (
    <motion.div
      className="epk-page"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      transition={{ duration: 0.5 }}
    >
      {/* Page Title */}
      <div className="epk-header">
        <h1>Electronic Press Kit</h1>
        <p className="epk-subtitle">Ghost Pavilion</p>
      </div>

      {/* Playlist Pitch */}
      <motion.section
        className="epk-section epk-pitch-section"
        initial={{ opacity: 0, y: 20 }}
        whileInView={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        viewport={{ once: true }}
      >
        <h2>Curator Pitch</h2>
        <p className="epk-pitch">
          A dark, atmospheric indie track with dreamy guitars, moody synth
          layers, and an emotional slow-groove feel. "No Way To Love" explores
          the quiet intensity of losing someone and the way grief transforms
          memory. Ideal for playlists centering on introspective, cinematic, and
          late-night moods.
        </p>
      </motion.section>

      {/* Artist Overview */}
      <motion.section
        className="epk-section"
        initial={{ opacity: 0, y: 20 }}
        whileInView={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        viewport={{ once: true }}
      >
        <h2>Artist Overview</h2>
        <div className="epk-details">
          <div className="epk-detail-row">
            <span className="epk-label">Artist Name</span>
            <span className="epk-value">Ghost Pavilion</span>
          </div>
          <div className="epk-detail-row">
            <span className="epk-label">Location</span>
            <span className="epk-value">Los Angeles, CA</span>
          </div>
          <div className="epk-detail-row">
            <span className="epk-label">Genres</span>
            <span className="epk-value">
              Dreamy Indie, Atmospheric, Indie Rock
            </span>
          </div>
          <div className="epk-detail-row">
            <span className="epk-label">For Fans Of</span>
            <span className="epk-value">
              Beach House, The National, Scott Walker, David Bowie
            </span>
          </div>
        </div>

        <div className="epk-bio">
          <h3>Bio</h3>
          <p>
            Ghost Pavilion is a Los Angeles–based indie project blending moody
            textures, dreamy guitars, and cinematic atmospheres to explore themes
            of memory, grief, and emotional distance. The project lives in the
            space between intimacy and detachment, pairing slow-burning grooves
            with melancholic melodies and subtle electronic elements. Influenced
            by artists like Beach House, The National, and the darker, more
            experimental edges of classic art pop, Ghost Pavilion leans into
            emotional restraint rather than big dramatic gestures. The music
            often reflects the quiet weight of loss and the strange numbness that
            can follow it. Each release builds toward a more immersive and
            emotionally focused sonic world.
          </p>
        </div>
      </motion.section>

      {/* Latest Release */}
      <motion.section
        className="epk-section"
        initial={{ opacity: 0, y: 20 }}
        whileInView={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        viewport={{ once: true }}
      >
        <h2>Latest Release</h2>
        <div className="epk-details">
          <div className="epk-detail-row">
            <span className="epk-label">Title</span>
            <span className="epk-value">No Way To Love</span>
          </div>
          <div className="epk-detail-row">
            <span className="epk-label">Release Date</span>
            <span className="epk-value">February 20, 2026</span>
          </div>
          <div className="epk-detail-row">
            <span className="epk-label">Genre</span>
            <span className="epk-value">Dreamy Indie, Atmospheric</span>
          </div>
          <div className="epk-detail-row">
            <span className="epk-label">Mood / Vibe</span>
            <span className="epk-value">
              Dark, emotional, slow-groove, cinematic
            </span>
          </div>
        </div>

        <div className="epk-bio">
          <h3>Short Description</h3>
          <p>
            A haunting, atmospheric indie track that explores grief not as a
            single moment, but as something that quietly lingers and reshapes
            memory.
          </p>
        </div>

        <div className="epk-bio">
          <h3>Press Release</h3>
          <p>
            Los Angeles–based indie project Ghost Pavilion returns with "No Way
            To Love," a haunting and emotionally charged new single arriving
            February 20, 2026. The track blends dreamy atmosphere, textured
            guitars, and a slow-burning groove to explore the quiet, complex
            landscape of losing someone you love.
          </p>
          <p>
            Built around funk-inflected electric guitars, moody synth pads,
            programmed drums, and a pulsing bass line, "No Way To Love" creates
            a cinematic world where nostalgia and darkness coexist. The vocals
            move with a dramatic intensity, drawing listeners into a deeply
            intimate exploration of grief, not as a moment, but as a lingering
            presence that reshapes the way love is remembered.
          </p>
          <p>
            "'No Way To Love' came from trying to live with the grief of knowing
            when someone is no longer here," says James, the mind behind Ghost
            Pavilion. "It's about the way you search for pieces of them in
            memory, and how love takes on a different form after loss."
          </p>
          <p>
            The track marks the beginning of a new creative era for Ghost
            Pavilion — richer textures, deeper emotional resonance, and a more
            expansive sonic world. It's a song that invites listeners to sit with
            their own memories, their own echoes, their own tenderness.
          </p>
          <p>
            "No Way To Love" releases February 20, 2026 on all streaming
            platforms.
          </p>
        </div>
      </motion.section>

      {/* Media */}
      <motion.section
        className="epk-section"
        initial={{ opacity: 0, y: 20 }}
        whileInView={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        viewport={{ once: true }}
      >
        <h2>Media</h2>
        <p className="epk-media-note">
          Press photos, cover art, and logo available for download.
        </p>
        <div className="epk-media-grid">
          <div className="epk-media-item">
            <img src={pressPhoto1} alt="Ghost Pavilion press photo 1 by Lauren Chang" />
            <div className="epk-media-info">
              <span>Press Photo 1</span>
              <a href={pressPhoto1} download="ghost-pavilion-press-photo-1.jpg">
                Download
              </a>
            </div>
          </div>
          <div className="epk-media-item">
            <img src={pressPhoto2} alt="Ghost Pavilion press photo 2 by Lauren Chang" />
            <div className="epk-media-info">
              <span>Press Photo 2</span>
              <a href={pressPhoto2} download="ghost-pavilion-press-photo-2.jpg">
                Download
              </a>
            </div>
          </div>
          <div className="epk-media-item">
            <img src={albumArt} alt="Ghost Pavilion album art" />
            <div className="epk-media-info">
              <span>Album Art</span>
              <a href={albumArt} download="ghost-pavilion-album-art.png">
                Download
              </a>
            </div>
          </div>
        </div>
      </motion.section>

      {/* Links */}
      <motion.section
        className="epk-section"
        initial={{ opacity: 0, y: 20 }}
        whileInView={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        viewport={{ once: true }}
      >
        <h2>Links</h2>
        <div className="epk-links">
          <a
            href="https://open.spotify.com/artist/6e1gGZhzHrDzdI3voe9FxV"
            target="_blank"
            rel="noopener noreferrer"
          >
            Spotify
          </a>
          <a
            href="https://www.youtube.com/@ghost_pavilion"
            target="_blank"
            rel="noopener noreferrer"
          >
            YouTube
          </a>
          <a
            href="https://www.instagram.com/ghost_pavilion/"
            target="_blank"
            rel="noopener noreferrer"
          >
            Instagram
          </a>
          <a
            href="https://www.facebook.com/GhostPavilion"
            target="_blank"
            rel="noopener noreferrer"
          >
            Facebook
          </a>
          <a
            href="https://www.tiktok.com/@ghost_pavilion"
            target="_blank"
            rel="noopener noreferrer"
          >
            TikTok
          </a>
        </div>
      </motion.section>

      {/* Contact */}
      <motion.section
        className="epk-section"
        initial={{ opacity: 0, y: 20 }}
        whileInView={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        viewport={{ once: true }}
      >
        <h2>Contact</h2>
        <div className="epk-details">
          <div className="epk-detail-row">
            <span className="epk-label">Artist</span>
            <span className="epk-value">Ghost Pavilion</span>
          </div>
          <div className="epk-detail-row">
            <span className="epk-label">Email</span>
            <span className="epk-value">
              <a href="mailto:info@ghostpavilion.com">info@ghostpavilion.com</a>
            </span>
          </div>
        </div>
      </motion.section>
    </motion.div>
  );
};

export default EPKPage;
