import { motion } from "framer-motion";
import "./ListenPage.css";

const spotifyEmbeds = [
  {
    title: "No Way to Love",
    src: "https://open.spotify.com/embed/album/4JtF4aERTSH2CA3MQ3k99K?utm_source=generator&theme=0",
  },
  {
    title: "Ghost Pavilion",
    src: "https://open.spotify.com/embed/album/5qMmsMgU9QzzSr9ju9PVjF?utm_source=generator&theme=0",
  },
  {
    title: "Fallout",
    src: "https://open.spotify.com/embed/album/726ibupVS8kT5uQxBmHti8?utm_source=generator&theme=0",
  },
  {
    title: "Bleed on Sunset",
    src: "https://open.spotify.com/embed/album/3XlzaJpG7kDQOL73bldhjB?utm_source=generator&theme=0",
  },
  {
    title: "Oblivion",
    src: "https://open.spotify.com/embed/album/2m0zn2vUaVVuVXlpqhIcgW?utm_source=generator&theme=0",
  },
  {
    title: "Traces",
    src: "https://open.spotify.com/embed/album/1b9PrJzDEVwc79V53ep1XG?utm_source=generator&theme=0",
  },
];

// BANDCAMP VERSION — uncomment below and swap into the render to revert
// const bandcampEmbeds = [
//   {
//     title: "ghost-pavilion",
//     src: "https://bandcamp.com/EmbeddedPlayer/album=3819933139/size=large/bgcol=333333/linkcol=0f91ff/tracklist=false/transparent=true/",
//     link: "https://ghostpavilion.bandcamp.com/track/fallout-2",
//     text: "Ghost Pavilion by Ghost Pavilion",
//     type: "album",
//   },
//   {
//     title: "ghost-pavilion-fallout",
//     src: "https://bandcamp.com/EmbeddedPlayer/track=3117515333/size=large/bgcol=333333/linkcol=0f91ff/tracklist=false/transparent=true/",
//     link: "https://ghostpavilion.bandcamp.com/track/fallout-2",
//     text: "Fallout by Ghost Pavilion",
//     type: "track",
//   },
//   {
//     title: "bleed-on-sunset",
//     src: "https://bandcamp.com/EmbeddedPlayer/track=77723839/size=large/bgcol=333333/linkcol=0f91ff/tracklist=false/transparent=true/",
//     link: "http://ghostpavilion.bandcamp.com/track/bleed-on-sunset",
//     text: "Bleed on Sunset by Ghost Pavilion",
//     type: "track",
//   },
//   {
//     title: "oblivion",
//     src: "https://bandcamp.com/EmbeddedPlayer/album=2411569131/size=large/bgcol=333333/linkcol=0f91ff/tracklist=false/transparent=true/",
//     link: "http://ghostpavilion.bandcamp.com/album/oblivion",
//     text: "Oblivion by Ghost Pavilion",
//     type: "album",
//   },
//   {
//     title: "traces",
//     src: "https://bandcamp.com/EmbeddedPlayer/album=3727972298/size=large/bgcol=333333/linkcol=0f91ff/tracklist=false/transparent=true/",
//     link: "http://ghostpavilion.bandcamp.com/album/traces",
//     text: "Traces by Ghost Pavilion",
//     type: "album",
//   },
// ];

const ListenPage = () => {
  return (
    <div className="listenpage">
      {spotifyEmbeds.map(({ title, src }, index) => (
        <motion.section
          className="spotify-embed-section"
          key={index}
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5, ease: "easeOut" }}
          viewport={{ once: true }}
        >
          <div className="spotify-wrapper">
            <iframe
              title={title}
              src={src}
              width="100%"
              height="380"
              frameBorder="0"
              allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
              loading="lazy"
            ></iframe>
          </div>
        </motion.section>
      ))}
    </div>
  );
};

export default ListenPage;
