import { motion } from "framer-motion";
import "./WatchPage.css";

const videos = [
  { title: "nowaytolove", src: "https://www.youtube.com/embed/5Sdu-ANN16Q" },
  { title: "allalong", src: "https://www.youtube.com/embed/tjZYOAoTwCg" },
  { title: "hush", src: "https://www.youtube.com/embed/MjMjeyqyddM" },
  { title: "lastseason", src: "https://www.youtube.com/embed/mgQRL8IW6bc" },
  {
    title: "servesyouright_live",
    src: "https://www.youtube.com/embed/y7y8wi7KHdY",
  },
  { title: "servesyouright", src: "https://www.youtube.com/embed/Ak2U6AmenBk" },
  { title: "shouldofknown", src: "https://www.youtube.com/embed/baqUc9pGCrM" },
  { title: "troubleisee", src: "https://www.youtube.com/embed/bDQN5GN4xcg" },
  {
    title: "stillonice_live",
    src: "https://www.youtube.com/embed/viaidZnToJg",
  },
  { title: "stillonice", src: "https://www.youtube.com/embed/U-yPOqWZt5I" },
  { title: "fallout_live", src: "https://www.youtube.com/embed/U3wLO-caWxo" },
  { title: "fallout", src: "https://www.youtube.com/embed/eTaPTcasXYc" },
  { title: "bleedonsunset", src: "https://www.youtube.com/embed/6-7XeKJjPcI" },
  { title: "bleedonsunset", src: "https://www.youtube.com/embed/r_8kucOarSk" },
  { title: "livevideo", src: "https://www.youtube.com/embed/dTvuJnkLECw" },
  { title: "vacantstories", src: "https://www.youtube.com/embed/zvsYVJa-D_8" },
  { title: "blackandblue", src: "https://www.youtube.com/embed/7Uu_pHFaeuo" },
];

const WatchPage = () => {
  return (
    <div className="watchpage">
      {videos.map((video, index) => (
        <motion.section
          className="video-spacing"
          key={index}
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5, ease: "easeOut" }}
          viewport={{ once: true }}
        >
          <div className="video-wrapper">
            <iframe
              className="videos"
              title={video.title}
              src={video.src}
              frameBorder="0"
              allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
              allowFullScreen
            ></iframe>
          </div>
        </motion.section>
      ))}
    </div>
  );
};

export default WatchPage;
