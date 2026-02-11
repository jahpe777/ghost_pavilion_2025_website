import { Route, Routes } from "react-router-dom";
import { AnimatePresence } from "framer-motion";

import "./App.css";

import NavBar from "./NavBar/NavBar";
import Footer from "./Footer/Footer";
import LandingPage from "./LandingPage/LandingPage";
import WatchPage from "./WatchPage/WatchPage";
import ListenPage from "./ListenPage/ListenPage";
import SignUpPage from "./SignUpPage/SignUpPage";
import EPKPage from "./EPKPage/EPKPage";

const App = () => {
  return (
    <div className="App">
      <header className="App-Header">
        <Routes>
          <Route path="/*" element={<NavBar />} />
        </Routes>
      </header>
      <main className="Header">
        <AnimatePresence mode="wait">
          <Routes>
            <Route path="/" element={<LandingPage />} />
            <Route path="/watch" element={<WatchPage />} />
            <Route path="/listen" element={<ListenPage />} />
            <Route path="/signup" element={<SignUpPage />} />
            <Route path="/epk" element={<EPKPage />} />
          </Routes>
        </AnimatePresence>
      </main>
      <footer>
        <Routes>
          <Route path="/*" element={<Footer />} />
        </Routes>
      </footer>
    </div>
  );
};

export default App;
