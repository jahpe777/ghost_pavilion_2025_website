# Ghost Pavilion - Complete Project Documentation

**Artist/Project:** Ghost Pavilion
**Owner:** James Higgs
**Business Type:** Sole Proprietorship
**EIN:** Obtained October 2024
**Repository:** https://github.com/jahpe777/ghost_pavilion_2025

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Business Setup](#business-setup)
3. [Website Architecture](#website-architecture)
4. [Music Distribution Strategy](#music-distribution-strategy)
5. [Email Marketing System](#email-marketing-system)
6. [Social Media & Advertising](#social-media--advertising)
7. [Technology Stack](#technology-stack)
8. [Roadmap & Next Steps](#roadmap--next-steps)

---

## Project Overview

Ghost Pavilion is a music project with an integrated web presence, email marketing system, and multi-platform distribution strategy. The project focuses on electronic/experimental music with a strong visual and digital presence.

### Key Objectives
- Build engaged fan base through email list
- Distribute music across all major streaming platforms
- Run targeted advertising campaigns on Meta platforms
- Create AI-generated music videos for releases
- Maintain professional web presence at ghostpavilion.com

---

## Business Setup

### Legal Structure
- **Business Name:** Ghost Pavilion
- **Structure:** Sole Proprietorship
- **Owner:** James Higgs
- **EIN:** Obtained specifically for Meta Business verification (October 2024)

### Purpose of EIN
- Originally obtained to verify Meta Business account for advanced analytics
- Enables business features on Facebook/Instagram advertising
- Provides professional business identity for music project

### Meta Business Verification Status
- **Status:** Attempted but not completed (October 2024)
- **Issue:** Meta's document upload system repeatedly failed when trying to submit EIN documentation
- **Decision:** Proceeding without verification initially
  - Can still run basic ad campaigns
  - Can access essential analytics
  - Verification can be completed later if needed for advanced features

---

## Website Architecture

### Domain & Hosting
- **Domain:** ghostpavilion.com (and www.ghostpavilion.com)
- **Frontend Hosting:** Vercel
- **Backend Hosting:** Railway (in progress)
- **Database:** PostgreSQL on Railway

### Frontend (React + Vite)
**Location:** `frontend/` directory

**Technology:**
- React 18
- TypeScript
- Vite (migrated from Create React App)
- Framer Motion (animations)
- React Router (navigation)

**Pages:**
1. **Landing Page** (`/`)
   - Ghost Pavilion logo/album art
   - "LISTEN NOW" button → Toneden smart link
   - Animated background overlay
   - Background video element
   - Email signup form integration

2. **Music Page** (`/listen`)
   - Streaming platform links
   - Embedded players (if applicable)
   - Toneden smart link integration

3. **Videos Page** (`/watch`)
   - Music video embeds
   - Visual content
   - AI-generated music videos (planned)

4. **Sign Up Page** (`/signup`)
   - Email collection form
   - Connected to Django backend
   - Triggers SendGrid welcome email

**Navigation:**
- Home
- Music (formerly "Listen")
- Videos (formerly "Watch")
- Sign Up

**Footer Links (Simplified to 4 essential links):**
1. 🎵 Toneden (https://fanlink.tv/ghostpavilion) - Music icon
2. 📷 Instagram (@ghost_pavilion)
3. 🎵 TikTok (@ghostpavilion)
4. ✉️ Email (info@ghostpavilion.com)

**Design Elements:**
- Dark theme
- Custom font: "Fugue"
- Primary colors: White text, orange accents (#ff6600)
- Animated elements with Framer Motion
- Responsive design for mobile/desktop

### Backend (Django REST API)
**Location:** `backend/` directory

**Technology:**
- Django 5.2
- Django REST Framework
- PostgreSQL database
- SendGrid email integration
- CORS headers for frontend communication

**API Endpoints:**
- `/api/signup/` - Email subscription endpoint

**Apps:**
1. **Mailing App**
   - Subscriber model (email field)
   - SignUpCreateView (REST API endpoint)
   - SendGrid integration for welcome emails
   - Management command for mass emails

**Database Schema:**
```
Subscriber
├── id (auto)
├── email (unique, required)
├── created_at (auto)
└── updated_at (auto)
```

**Email Features:**
- Welcome email on signup (HTML template with Ghost Pavilion branding)
- Mass email capability via Django management command
- Duplicate prevention
- Email validation

---

## Music Distribution Strategy

### Streaming Platforms
Music is distributed across all major platforms via standard distribution service (DistroKid, TuneCore, or similar).

**Key Platforms:**
- Spotify
- Apple Music
- YouTube Music
- Amazon Music
- Tidal
- Deezer
- Pandora
- SoundCloud
- Bandcamp

### Toneden Smart Link Integration
**URL:** https://fanlink.tv/ghostpavilion

**Purpose:** Single link that directs fans to Ghost Pavilion music on their preferred streaming platform

**Integration Points:**
1. **Website Landing Page:** Prominent "LISTEN NOW" button
2. **Footer:** Music icon link in simplified footer
3. **Social Media:** Primary link in bio across all platforms
4. **Email Marketing:** Included in welcome emails and newsletters

**Benefits:**
- Single link to share everywhere
- Fans automatically directed to their preferred platform
- Analytics on which platforms fans use
- Professional presentation
- Easy to update when new releases drop

### Release Strategy
1. **Pre-Release Phase:**
   - Build email list through website
   - Tease on social media (Instagram, TikTok)
   - Create AI-generated music video

2. **Release Day:**
   - Update Toneden link with new release
   - Send mass email to subscriber list via Django command
   - Post to all social platforms
   - Run Meta ad campaigns targeting music listeners

3. **Post-Release:**
   - Monitor analytics (streaming platforms + Meta)
   - Engage with fans via email and social
   - Plan next release/content

---

## Email Marketing System

### SendGrid Setup
- **Service:** SendGrid
- **Sender Email:** info@ghostpavilion.com
- **Authentication:** Domain verified
- **Status:** ✅ Complete and operational

### Email Types

#### 1. Welcome Email (Automated)
**Trigger:** New signup via website
**Template:** Professional HTML email with Ghost Pavilion branding
**Content:**
- Welcome message
- Links to streaming platforms (via Toneden)
- Social media links
- Branded design matching website aesthetic

#### 2. Mass Emails (Manual via Django)
**Command:** `python manage.py send_mass_email "Subject" "Message"`
**Use Cases:**
- New release announcements
- Show announcements
- Special content drops
- Fan engagement

**Best Practices:**
- Limit frequency to avoid unsubscribes
- Provide value (exclusive content, early access, etc.)
- Include Toneden link for easy music access
- Keep concise and on-brand

### Subscriber Management
- All subscribers stored in PostgreSQL database
- Accessible via Django admin panel
- Can export for analysis
- Duplicate prevention built-in

---

## Social Media & Advertising

### Social Media Presence

**Instagram:** @ghost_pavilion
- Primary visual platform
- Behind-the-scenes content
- Music snippets/teasers
- Link in bio → Toneden

**TikTok:** @ghostpavilion
- Music discovery platform
- Short-form video content
- Trending sounds/challenges
- Link in bio → Toneden

**YouTube:** (Implied for music videos)
- Music videos (including AI-generated)
- Full track uploads
- Visual content

### Meta Business Manager
**Purpose:** Centralized hub for Facebook/Instagram advertising and analytics

**Current Status:**
- Account created and configured
- Business verification attempted but not completed
- Can run ads without verification (with some limitations)
- Can access basic analytics

**Advertising Strategy:**

#### Target Audience
- Music listeners (electronic/experimental genres)
- Age: 18-45
- Interests: Similar artists, music festivals, streaming platforms
- Geographic: Start local/regional, expand based on performance

#### Ad Types to Explore
1. **Awareness Campaigns**
   - Introduce Ghost Pavilion to new audiences
   - Focus on Toneden link clicks
   - Video content (snippets, teasers)

2. **Engagement Campaigns**
   - Build social media following
   - Encourage shares/saves
   - Community building

3. **Conversion Campaigns**
   - Email signups
   - Streaming platform follows
   - Show ticket sales (future)

#### Budget & Approach
- Start small to test what works
- A/B test different creatives and copy
- Monitor analytics closely
- Scale what performs well
- Can start without business verification

**Analytics Access:**
- Track ad performance
- Understand audience demographics
- Monitor engagement rates
- Optimize campaigns based on data

---

## Technology Stack

### Frontend
```
Technology: React 18 + TypeScript + Vite
Hosting: Vercel
URL: https://ghostpavilion.com
Key Libraries:
  - framer-motion (animations)
  - react-router-dom (navigation)
  - react-icons (social icons)
```

### Backend
```
Technology: Django 5.2 + Django REST Framework
Hosting: Railway
Database: PostgreSQL (Railway)
Key Packages:
  - django-cors-headers (frontend communication)
  - sendgrid (email)
  - psycopg2-binary (PostgreSQL)
  - gunicorn (production server)
  - dj-database-url (Railway database config)
```

### Email
```
Service: SendGrid
Sender: info@ghostpavilion.com
Features:
  - Automated welcome emails
  - Mass email campaigns
  - HTML email templates
```

### Music Distribution
```
Smart Link: Toneden (fanlink.tv/ghostpavilion)
Platforms: All major streaming services
Management: Via music distributor
```

### Development Tools
```
Version Control: Git + GitHub
Package Management: npm (frontend), pip (backend)
Environment: Python 3.12, Node.js 20.x
Local Database: PostgreSQL
```

---

## Roadmap & Next Steps

### Immediate Priorities (Current Phase)

#### 1. ✅ COMPLETE: Website Migration
- [x] Migrate from Create React App to Vite
- [x] Deploy frontend to Vercel
- [x] Update navigation labels
- [x] Simplify footer to essential links
- [x] Add Toneden "LISTEN NOW" button

#### 2. ⏳ IN PROGRESS: Backend Deployment
- [x] Configure Django for production
- [x] Create Railway project
- [x] Set up PostgreSQL database
- [x] Configure environment variables
- [ ] **BLOCKED:** Fix Postgres service in Railway
- [ ] Complete Django deployment
- [ ] Run database migrations
- [ ] Test email signup end-to-end
- [ ] Update frontend with production API endpoint

#### 3. ⏸️ PENDING: SendGrid Sender Verification
- [x] Basic SendGrid setup complete
- [ ] Verify full sender authentication
- [ ] Test email deliverability
- [ ] Ensure emails don't go to spam

#### 4. ⏸️ PENDING: Meta Advertising Campaign
**Goal:** Create first ad campaign to drive traffic to Toneden link and grow email list

**Steps:**
1. Define campaign objective (awareness vs. conversion)
2. Set budget ($50-100 to start)
3. Create ad creative (images/video + copy)
4. Define target audience
5. Launch campaign
6. Monitor and optimize

**Note:** Can proceed without business verification

### Short-Term Goals (Next 30 Days)

#### 1. AI Music Video Creation
**Purpose:** Create engaging visual content for next release

**Approach:**
- Research AI video generation tools (Runway, Pika, etc.)
- Match visual aesthetic to Ghost Pavilion brand
- Create 1-2 videos for upcoming releases
- Upload to YouTube
- Share across social media

**Benefits:**
- More shareable content
- Better Meta ad performance (video ads)
- Professional presentation
- Stand out from audio-only releases

#### 2. Email List Growth
**Target:** Grow subscriber base to 100+ before next release

**Methods:**
- Meta ad campaigns
- Social media CTAs
- Exclusive content offers
- Toneden integration (consider Toneden email capture)

#### 3. Release Preparation
**Activities:**
- Finalize next track for release
- Create AI music video
- Write email announcement copy
- Prepare social media content calendar
- Set up Meta ad campaign for release day

### Medium-Term Goals (3-6 Months)

1. **Consistent Release Schedule**
   - Establish regular release cadence (monthly/bi-monthly)
   - Build anticipation with teasers
   - Grow streaming platform followers

2. **Email Engagement**
   - Send monthly newsletters
   - Provide exclusive content to subscribers
   - Track open rates and engagement
   - Refine email strategy based on data

3. **Social Media Growth**
   - Post consistently on Instagram/TikTok
   - Engage with similar artists/fans
   - Experiment with different content types
   - Build community

4. **Analytics & Optimization**
   - Monitor streaming platform analytics
   - Track Meta ad performance
   - Analyze email metrics
   - Website traffic analysis (add Google Analytics)
   - Adjust strategy based on data

### Long-Term Vision (6-12 Months)

1. **Established Fan Base**
   - 500+ email subscribers
   - 1000+ social media followers
   - Consistent streaming numbers
   - Engaged community

2. **Revenue Streams**
   - Streaming royalties
   - Bandcamp sales (physical/digital)
   - Show opportunities
   - Merchandise (future)

3. **Professional Presence**
   - Consistent brand across all platforms
   - Regular content output
   - Industry connections
   - Media features/playlists

4. **Technical Improvements**
   - Custom merch store integration
   - Advanced analytics dashboard
   - Show booking system
   - Member-only content area

---

## Content Strategy

### Website
- **Update Frequency:** As needed for releases
- **Primary CTA:** Email signup + Toneden link
- **Content Focus:** Music discovery and fan connection

### Email (SendGrid)
- **Welcome Email:** Immediate upon signup
- **Newsletters:** Monthly (minimum)
- **Release Announcements:** Every release
- **Exclusive Content:** Quarterly
- **Tone:** Personal, direct, value-driven

### Social Media
**Instagram:**
- Frequency: 3-4x per week
- Content: Visual aesthetic, music snippets, behind-the-scenes
- Stories: Daily engagement

**TikTok:**
- Frequency: 2-3x per week
- Content: Short music clips, trending sounds, personality
- Focus: Discovery algorithm

### Advertising (Meta)
**Investment:** Start with $50-100/month
**Focus:**
- Email list growth
- Toneden link clicks
- Social media following
**Measurement:**
- Cost per signup
- Link click-through rate
- Follower growth rate

---

## File Structure

```
ghost-pavilion-website-2025/
├── frontend/
│   ├── src/
│   │   ├── App.tsx
│   │   ├── App.css
│   │   ├── LandingPage/
│   │   │   ├── LandingPage.tsx
│   │   │   └── LandingPage.css
│   │   ├── ListenPage/
│   │   │   ├── ListenPage.tsx (Music page)
│   │   │   └── ListenPage.css
│   │   ├── WatchPage/
│   │   │   ├── WatchPage.tsx (Videos page)
│   │   │   └── WatchPage.css
│   │   ├── SignUpPage/
│   │   │   ├── SignUpPage.tsx
│   │   │   └── SignUpPage.css
│   │   ├── NavBar/
│   │   │   ├── NavBar.tsx
│   │   │   └── NavBar.css
│   │   ├── Footer/
│   │   │   ├── Footer.tsx
│   │   │   └── Footer.css
│   │   └── Images/
│   ├── public/
│   ├── package.json
│   ├── vite.config.ts
│   └── vercel.json
├── backend/
│   ├── ghostpavilion_backend/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── mailing/
│   │   ├── models.py
│   │   ├── views.py
│   │   └── management/
│   │       └── commands/
│   │           └── send_mass_email.py
│   ├── manage.py
│   ├── requirements.txt
│   ├── runtime.txt
│   ├── Procfile
│   └── start.sh
├── env/ (local only, not in git)
├── SESSION_HISTORY.md
├── GHOST_PAVILION_PROJECT.md (this file)
└── README.md
```

---

## Key URLs & Links

### Public URLs
- **Website:** https://ghostpavilion.com
- **Toneden Smart Link:** https://fanlink.tv/ghostpavilion
- **Instagram:** https://www.instagram.com/ghost_pavilion
- **TikTok:** https://www.tiktok.com/@ghostpavilion
- **Email:** info@ghostpavilion.com

### Admin/Development
- **GitHub Repository:** https://github.com/jahpe777/ghost_pavilion_2025
- **Vercel Dashboard:** (Frontend hosting)
- **Railway Dashboard:** https://railway.com/project/fc1c8f74-16d6-458d-8093-7154c443f48a
- **SendGrid Dashboard:** (Email management)
- **Meta Business Manager:** (Advertising)

---

## Commands Quick Reference

### Local Development

**Frontend:**
```bash
cd frontend
npm install
npm run dev          # Development server
npm run build        # Production build
```

**Backend:**
```bash
cd backend
source ../env/bin/activate    # Activate virtual environment
pip install -r requirements.txt
python manage.py runserver    # Development server
python manage.py migrate      # Run migrations
python manage.py send_mass_email "Subject" "Message"  # Send newsletter
```

### Deployment

**Frontend (Vercel):**
- Automatic deployment on git push to master
- Manual deployment: `vercel --prod`

**Backend (Railway):**
```bash
railway login
railway link          # Link to project
railway up            # Deploy
railway logs          # View logs
railway variables     # Manage environment variables
railway domain        # Generate public domain
```

**Git:**
```bash
git add .
git commit -m "message"
git push origin master
```

---

## Success Metrics

### Website
- Email signups per month
- Unique visitors
- Toneden link clicks
- Time on site

### Email Marketing
- List growth rate
- Open rate (target: >20%)
- Click-through rate (target: >3%)
- Unsubscribe rate (keep <2%)

### Social Media
- Follower growth rate
- Engagement rate (likes, comments, shares)
- Link clicks to Toneden
- Content reach/impressions

### Music Streaming
- Monthly listeners
- Stream count
- Save rate
- Playlist additions

### Advertising
- Cost per email signup (target: <$2)
- Cost per Toneden link click (target: <$0.50)
- Return on ad spend (track streaming/engagement from ad traffic)

---

## Notes & Lessons Learned

### Technical
1. **Railway Deployment Complexity:** Railway is more complex than expected. Creating separate services for database vs. web app is not intuitive via CLI. Web dashboard is more reliable.

2. **Meta Business Verification:** EIN alone insufficient if Meta's upload system has technical issues. Can proceed with basic advertising without verification.

3. **Vercel Simplicity:** Vercel frontend deployment is straightforward and automatic with GitHub integration.

4. **SendGrid Reliability:** SendGrid setup was smooth. Professional sender email (info@ghostpavilion.com) adds credibility.

### Strategy
1. **Start Simple:** Don't need business verification or complex analytics to start growing. Focus on content and consistent output.

2. **Email List Priority:** Email list is owned audience (unlike social media). Make it a priority to grow organically and through ads.

3. **Toneden Value:** Single link simplifies everything. Use it everywhere.

4. **Content Consistency:** Better to post regularly with good content than sporadically with perfect content.

---

## Support & Resources

### Technical Documentation
- **Django:** https://docs.djangoproject.com/
- **React:** https://react.dev/
- **Railway:** https://docs.railway.app/
- **Vercel:** https://vercel.com/docs
- **SendGrid:** https://docs.sendgrid.com/

### Music Industry Resources
- **Toneden:** https://www.toneden.io/
- **Meta for Business:** https://www.facebook.com/business
- **Streaming Platform Analytics:** Available in each platform's artist dashboard

### AI Tools (for Music Videos)
- **Runway:** https://runwayml.com/
- **Pika:** https://pika.art/
- **Stable Diffusion:** Various implementations
- **Research ongoing**

---

## Project Status Summary

**Overall Progress:** 75% Complete

✅ **Completed:**
- Website design and development
- Frontend deployed to Vercel
- Email system configured (SendGrid)
- Business entity established (EIN obtained)
- Toneden integration
- Social media presence established
- GitHub repository organized

⏳ **In Progress:**
- Backend deployment to Railway (95% - minor blocker)
- Meta advertising setup (ready to launch campaigns)

⏸️ **Planned:**
- First Meta ad campaign
- AI music video creation
- Email list growth to 100+ subscribers
- Consistent release schedule

---

**Last Updated:** October 29, 2025
**Next Review:** After backend deployment completion

---

## Appendix: Business Contacts

### Service Providers
- **Domain Registrar:** (Add if relevant)
- **Email Hosting:** SendGrid
- **Web Hosting:** Vercel (frontend), Railway (backend)
- **Music Distribution:** (Add distributor name)

### Social Media Handles
- Instagram: @ghost_pavilion
- TikTok: @ghostpavilion
- YouTube: (Add if created)
- Facebook: (Add if created)

### Key Accounts
- GitHub: jahpe777
- Railway: James Higgs
- Vercel: (Connected to GitHub)
- SendGrid: info@ghostpavilion.com
- Meta Business Manager: Ghost Pavilion

---

*This document serves as the central reference for all Ghost Pavilion project activities, strategy, and technical implementation. Keep updated as project evolves.*
