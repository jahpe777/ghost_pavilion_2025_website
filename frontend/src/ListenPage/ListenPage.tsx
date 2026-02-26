import { motion } from "framer-motion";
import "./ListenPage.css";

const bandcampEmbeds = [
  {
    title: "no-way-to-love",
    src: "https://bandcamp.com/EmbeddedPlayer/track=1999556700/size=large/bgcol=333333/linkcol=0f91ff/tracklist=false/transparent=true/",
    link: "https://ghostpavilion.bandcamp.com/track/no-way-to-love",
    text: "No Way to Love by Ghost Pavilion",
    type: "track",
  },
  {
    title: "ghost-pavilion",
    src: "https://bandcamp.com/EmbeddedPlayer/album=3819933139/size=large/bgcol=333333/linkcol=0f91ff/tracklist=false/transparent=true/",
    link: "https://ghostpavilion.bandcamp.com/album/ghost-pavilion",
    text: "Ghost Pavilion by Ghost Pavilion",
    type: "album",
  },
  {
    title: "ghost-pavilion-fallout",
    src: "https://bandcamp.com/EmbeddedPlayer/track=3117515333/size=large/bgcol=333333/linkcol=0f91ff/tracklist=false/transparent=true/",
    link: "https://ghostpavilion.bandcamp.com/track/fallout-2",
    text: "Fallout by Ghost Pavilion",
    type: "track",
  },
  {
    title: "bleed-on-sunset",
    src: "https://bandcamp.com/EmbeddedPlayer/track=77723839/size=large/bgcol=333333/linkcol=0f91ff/tracklist=false/transparent=true/",
    link: "http://ghostpavilion.bandcamp.com/track/bleed-on-sunset",
    text: "Bleed on Sunset by Ghost Pavilion",
    type: "track",
  },
  {
    title: "oblivion",
    src: "https://bandcamp.com/EmbeddedPlayer/album=2411569131/size=large/bgcol=333333/linkcol=0f91ff/tracklist=false/transparent=true/",
    link: "http://ghostpavilion.bandcamp.com/album/oblivion",
    text: "Oblivion by Ghost Pavilion",
    type: "album",
  },
  {
    title: "traces",
    src: "https://bandcamp.com/EmbeddedPlayer/album=3727972298/size=large/bgcol=333333/linkcol=0f91ff/tracklist=false/transparent=true/",
    link: "http://ghostpavilion.bandcamp.com/album/traces",
    text: "Traces by Ghost Pavilion",
    type: "album",
  },
];

const ListenPage = () => {
  return (
    <div className="listenpage">
      {bandcampEmbeds.map(({ title, src, link, text, type }, index) => (
        <motion.section
          className="bandcamp-embeds"
          key={index}
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5, ease: "easeOut" }}
          viewport={{ once: true }}
        >
          <div
            className={`bandcamp-wrapper ${
              type === "track" ? "adjusted-track" : ""
            }`}
          >
            <iframe title={title} src={src} seamless>
              <a href={link}>{text}</a>
            </iframe>
          </div>
        </motion.section>
      ))}
    </div>
  );
};

export default ListenPage;
