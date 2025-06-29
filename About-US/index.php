<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>About Us | RAISE Program</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
  <style>
    :root {
      --primary-green: #22663D;
      --hover-green: #B2FF59;
      --light-gray: #f5f5f5;
      --medium-gray: #e0e0e0;
      --dark-gray: #333;
      --white: #ffffff;
      --shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      --shadow-hover: 0 8px 15px rgba(0, 0, 0, 0.2);
      --transition: all 0.3s ease;
      --transition-slow: all 0.6s cubic-bezier(0.25, 1, 0.5, 1);
    }

    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      line-height: 1.8;
      color: var(--dark-gray);
      background-color: var(--white);
      overflow-x: hidden;
    }

    .container {
      width: 100%;
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 20px;
    }

    /* Navbar Styles */
    .navbar {
      background-color: var(--white);
      box-shadow: var(--shadow);
      position: sticky;
      top: 0;
      z-index: 1000;
      padding: 15px 0;
      transition: var(--transition);
    }

    .navbar:hover {
      box-shadow: var(--shadow-hover);
    }

    .navbar .container {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .logo {
      text-decoration: none;
      color: var(--primary-green);
      font-weight: 700;
      font-size: 1.5rem;
      display: flex;
      flex-direction: column;
      transition: var(--transition);
    }

    .logo:hover {
      color: var(--hover-green);
      transform: translateX(5px);
    }

    .logo span {
      font-size: 0.7rem;
      font-weight: 400;
      color: var(--dark-gray);
      margin-top: 3px;
    }

    .nav-links {
      display: flex;
      list-style: none;
      gap: 25px;
    }

    .nav-links a {
      text-decoration: none;
      color: var(--dark-gray);
      font-weight: 500;
      position: relative;
      padding: 5px 0;
      transition: var(--transition);
    }

    .nav-links a::after {
      content: '';
      position: absolute;
      bottom: 0;
      left: 0;
      width: 0;
      height: 2px;
      background-color: var(--hover-green);
      transition: var(--transition);
    }

    .nav-links a:hover {
      color: var(--primary-green);
    }

    .nav-links a:hover::after {
      width: 100%;
    }

    .nav-links .active {
      color: var(--primary-green);
      font-weight: 600;
    }

    .nav-links .active::after {
      width: 100%;
    }

    .dropdown {
      position: relative;
    }

    .dropdown-content {
      position: absolute;
      top: 100%;
      left: 0;
      background-color: var(--white);
      box-shadow: var(--shadow-hover);
      border-radius: 0 0 8px 8px;
      width: 250px;
      opacity: 0;
      visibility: hidden;
      transform: translateY(10px);
      transition: var(--transition);
      z-index: 100;
    }

    .dropdown:hover .dropdown-content {
      opacity: 1;
      visibility: visible;
      transform: translateY(0);
    }

    .dropdown-content a {
      display: block;
      padding: 12px 15px;
      border-bottom: 1px solid var(--medium-gray);
    }

    .dropdown-content a:hover {
      background-color: var(--light-gray);
    }

    .profile-icon img {
      border-radius: 50%;
      transition: var(--transition);
    }

    .profile-icon img:hover {
      transform: scale(1.1);
      box-shadow: 0 0 0 3px var(--hover-green);
    }

    /* Sliding Hero Section with Background Images */
    .sliding-hero {
      color: var(--white);
      text-align: center;
      margin-bottom: 60px;
      position: relative;
      overflow: hidden;
      height: 500px;
    }

    .hero-slide {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-size: cover;
      background-position: center;
      opacity: 0;
      transition: opacity 1.5s ease-in-out;
    }

    .hero-slide.active {
      opacity: 1;
    }

    .hero-slide:nth-child(1) {
      background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('https://images.unsplash.com/photo-1523961131990-5ea7c61b2107?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80');
    }

    .hero-slide:nth-child(2) {
      background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80');
    }

    .hero-slide:nth-child(3) {
      background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('https://images.unsplash.com/photo-1507679799987-c73779587ccf?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80');
    }

    .hero-content {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      width: 100%;
      padding: 0 20px;
    }

    .hero-content h1 {
      font-size: 3.5rem;
      margin-bottom: 20px;
      position: relative;
      display: inline-block;
      text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }

    .hero-content h1::after {
      content: '';
      position: absolute;
      bottom: -10px;
      left: 50%;
      transform: translateX(-50%);
      width: 100px;
      height: 4px;
      background-color: var(--hover-green);
      border-radius: 2px;
    }

    .hero-content p {
      font-size: 1.3rem;
      max-width: 800px;
      margin: 0 auto 30px;
      opacity: 0.9;
      text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
    }

    .hero-btn {
      display: inline-block;
      background-color: var(--hover-green);
      color: var(--dark-gray);
      padding: 12px 30px;
      border-radius: 30px;
      text-decoration: none;
      font-weight: 600;
      transition: var(--transition);
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    }

    .hero-btn:hover {
      background-color: var(--white);
      transform: translateY(-3px);
      box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3);
    }

    /* Mission/Vision Section */
    .mv-section {
      display: flex;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 30px;
      margin-bottom: 80px;
    }

    .mv-card {
      flex: 1;
      min-width: 300px;
      background-color: var(--white);
      border-radius: 12px;
      box-shadow: var(--shadow);
      padding: 40px 30px;
      text-align: center;
      transition: var(--transition);
      opacity: 0;
      transform: translateY(50px);
    }

    .mv-card.visible {
      opacity: 1;
      transform: translateY(0);
      transition: var(--transition-slow);
    }

    .mv-card:nth-child(1).visible {
      transition-delay: 0.1s;
    }
    .mv-card:nth-child(2).visible {
      transition-delay: 0.3s;
    }
    .mv-card:nth-child(3).visible {
      transition-delay: 0.5s;
    }

    .mv-card:hover {
      transform: translateY(-10px) !important;
      box-shadow: var(--shadow-hover);
    }

    .mv-icon {
      font-size: 3.5rem;
      color: var(--primary-green);
      margin-bottom: 25px;
      transition: var(--transition);
    }

    .mv-card:hover .mv-icon {
      color: var(--hover-green);
      transform: scale(1.1) rotate(5deg);
    }

    .mv-card h3 {
      font-size: 1.8rem;
      color: var(--primary-green);
      margin-bottom: 20px;
    }

    .mv-card p {
      font-size: 1.1rem;
      line-height: 1.9;
      margin-bottom: 20px;
    }

    /* About RAISE Program Section */
    .about-section {
      background-color: var(--light-gray);
      padding: 80px 0;
      margin-bottom: 80px;
      border-radius: 15px;
    }

    .about-section h2 {
      font-size: 2.5rem;
      color: var(--primary-green);
      margin-bottom: 30px;
      text-align: center;
      position: relative;
    }

    .about-section h2::after {
      content: '';
      position: absolute;
      bottom: -15px;
      left: 50%;
      transform: translateX(-50%);
      width: 80px;
      height: 4px;
      background-color: var(--hover-green);
      border-radius: 2px;
    }

    .about-section p {
      font-size: 1.15rem;
      line-height: 1.9;
      margin-bottom: 25px;
      max-width: 900px;
      margin-left: auto;
      margin-right: auto;
    }

    /* Org Structure Section */
    .org-section {
      margin-bottom: 80px;
    }

    .org-section h2 {
      font-size: 2.5rem;
      color: var(--primary-green);
      margin-bottom: 30px;
      text-align: center;
      position: relative;
    }

    .org-section h2::after {
      content: '';
      position: absolute;
      bottom: -15px;
      left: 50%;
      transform: translateX(-50%);
      width: 80px;
      height: 4px;
      background-color: var(--hover-green);
      border-radius: 2px;
    }

    .org-section p {
      font-size: 1.15rem;
      text-align: center;
      max-width: 700px;
      margin: 0 auto 40px;
      line-height: 1.8;
    }

    .org-chart {
      display: flex;
      flex-direction: column;
      align-items: center;
      margin-top: 40px;
    }

    .org-level {
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 30px;
      margin-bottom: 30px;
      width: 100%;
    }

    .org-item {
      background-color: var(--white);
      border-radius: 12px;
      box-shadow: var(--shadow);
      padding: 30px;
      text-align: center;
      transition: var(--transition);
      position: relative;
      overflow: hidden;
      z-index: 1;
      width: 100%;
      max-width: 280px;
      opacity: 0;
      transform: translateY(50px);
    }

    .org-item.visible {
      opacity: 1;
      transform: translateY(0);
      transition: var(--transition-slow);
    }

    .org-item:nth-child(1).visible {
      transition-delay: 0.2s;
    }
    .org-item:nth-child(2).visible {
      transition-delay: 0.4s;
    }
    .org-item:nth-child(3).visible {
      transition-delay: 0.6s;
    }

    .org-item::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 5px;
      background-color: var(--primary-green);
      transition: var(--transition);
    }

    .org-item:hover {
      transform: translateY(-10px) !important;
      box-shadow: var(--shadow-hover);
    }

    .org-item:hover::before {
      height: 10px;
      background-color: var(--hover-green);
    }

    .org-item h4 {
      color: var(--primary-green);
      margin-bottom: 15px;
      font-size: 1.4rem;
    }

    .org-item p {
      color: var(--dark-gray);
      margin-bottom: 20px;
      font-size: 1.1rem;
    }

    .org-item .org-img {
      width: 100px;
      height: 100px;
      border-radius: 50%;
      object-fit: cover;
      margin: 0 auto 20px;
      border: 3px solid var(--primary-green);
      transition: var(--transition);
    }

    .org-item:hover .org-img {
      border-color: var(--hover-green);
      transform: scale(1.05);
    }

    .director {
      max-width: 400px !important;
      background: linear-gradient(135deg, var(--white) 0%, var(--light-gray) 100%);
    }

    .director h4 {
      font-size: 1.8rem !important;
    }

    .director p {
      font-size: 1.3rem !important;
    }

    /* Footer */
    footer {
      background-color: var(--primary-green);
      color: var(--white);
      padding: 50px 0 30px;
      text-align: center;
      margin-top: 80px;
    }

    .footer-content {
      display: flex;
      justify-content: space-around;
      flex-wrap: wrap;
      gap: 30px;
      margin-bottom: 40px;
    }

    .footer-column {
      flex: 1;
      min-width: 250px;
      text-align: left;
    }

    .footer-column h3 {
      font-size: 1.3rem;
      margin-bottom: 20px;
      position: relative;
      display: inline-block;
    }

    .footer-column h3::after {
      content: '';
      position: absolute;
      bottom: -8px;
      left: 0;
      width: 40px;
      height: 2px;
      background-color: var(--hover-green);
    }

    .footer-column ul {
      list-style: none;
    }

    .footer-column li {
      margin-bottom: 10px;
    }

    .footer-column a {
      color: var(--white);
      text-decoration: none;
      transition: var(--transition);
      opacity: 0.8;
    }

    .footer-column a:hover {
      opacity: 1;
      color: var(--hover-green);
      padding-left: 5px;
    }

    .footer-bottom {
      padding-top: 30px;
      border-top: 1px solid rgba(255, 255, 255, 0.1);
    }

    .footer-bottom p {
      opacity: 0.8;
    }

    /* Scroll Animation */
    @keyframes fadeInUp {
      from {
        opacity: 0;
        transform: translateY(50px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }

    /* Responsive Design */
    @media (max-width: 992px) {
      .hero-content h1 {
        font-size: 2.8rem;
      }
      
      .org-level {
        flex-direction: column;
        align-items: center;
      }
    }

    @media (max-width: 768px) {
      .navbar .container {
        flex-direction: column;
      }
      
      .logo {
        margin-bottom: 15px;
      }
      
      .nav-links {
        flex-wrap: wrap;
        justify-content: center;
      }
      
      .hero-content h1 {
        font-size: 2.2rem;
      }
      
      .hero-content p {
        font-size: 1.1rem;
      }
      
      .sliding-hero {
        height: 450px;
      }
    }
  </style>
</head>
<body>
  <nav class="navbar">
    <div class="container">
      <a href="index.html" class="logo">RAISE Program <span>Research and Innovation for Sustainable Excellence</span></a>
      <ul class="nav-links">
        <li><a href="index.html">Home</a></li>
        <li class="dropdown">
          <a href="#">About US <i class="fas fa-chevron-down"></i></a>
          <div class="dropdown-content">
            <a href="raise.html">RAISE Program Overview</a>
            <a href="project1.html">Project 1: ABH</a>
            <a href="project2.html">Project 2: IPTM</a>
            <a href="project3.html">Project 3: ATBI</a>
            <a href="project4.html">Project 4: Knowledge Management</a>
          </div>
        </li>
        <li><a href="#">Resources</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
      <div class="profile-icon">
        <img src="https://via.placeholder.com/40" alt="User Icon">
      </div>
    </div>
  </nav>

  <!-- Sliding Hero with Background Images -->
  <div class="sliding-hero">
    <div class="hero-slide active">
      <div class="hero-content">
        <h1>Innovating for a Sustainable Future</h1>
        <p>The RAISE Program brings together leading researchers and innovators to tackle the world's most pressing challenges through interdisciplinary collaboration and cutting-edge technology.</p>
        <a href="#" class="hero-btn">Learn About Our Projects</a>
      </div>
    </div>
    <div class="hero-slide">
      <div class="hero-content">
        <h1>Our Vision for 2030</h1>
        <p>By 2030, we aim to establish RAISE as a global hub for sustainable innovation, with measurable impact across industries and communities worldwide through our research initiatives.</p>
        <a href="#" class="hero-btn">View Our Strategic Plan</a>
      </div>
    </div>
    <div class="hero-slide">
      <div class="hero-content">
        <h1>Join Our Network</h1>
        <p>We collaborate with academic institutions, industry partners, and government agencies to maximize the impact of our research. Explore partnership opportunities with RAISE.</p>
        <a href="#" class="hero-btn">Become a Partner</a>
      </div>
    </div>
  </div>

  <div class="container">
    <!-- Mission/Vision Section -->
    <div class="mv-section">
      <div class="mv-card" id="mission-card">
        <div class="mv-icon">
          <i class="fas fa-bullseye"></i>
        </div>
        <h3>Our Mission</h3>
        <p>The RAISE Program is dedicated to fostering innovation and research excellence through interdisciplinary collaboration. We develop sustainable solutions to complex challenges by bringing together experts from diverse fields including biotechnology, information technology, environmental science, and social innovation.</p>
        <p>Our approach combines fundamental research with practical applications, ensuring that our work translates into real-world impact. We measure our success not just by publications, but by the tangible benefits our research brings to communities and industries.</p>
      </div>
      
      <div class="mv-card" id="vision-card">
        <div class="mv-icon">
          <i class="fas fa-eye"></i>
        </div>
        <h3>Our Vision</h3>
        <p>To create a world where research and innovation work hand-in-hand to solve global challenges sustainably. We envision being the catalyst for transformative change through knowledge and technology.</p>
        <p>By 2030, RAISE aims to establish itself as a global leader in sustainable innovation, with our research directly contributing to at least 5 of the United Nations Sustainable Development Goals. We will achieve this through strategic partnerships, cutting-edge facilities, and a commitment to excellence in all our endeavors.</p>
      </div>
      
      <div class="mv-card" id="values-card">
        <div class="mv-icon">
          <i class="fas fa-heart"></i>
        </div>
        <h3>Our Values</h3>
        <p>Integrity, Collaboration, Innovation, Sustainability, and Excellence guide everything we do. These core values shape our research priorities and how we engage with partners and communities.</p>
        <p>We believe in transparent research practices, open collaboration across disciplines, and solutions that stand the test of time. Our team is committed to ethical research that benefits society while minimizing environmental impact. We hold ourselves to the highest standards of academic rigor and practical relevance.</p>
      </div>
    </div>

    <!-- About RAISE Section -->
    <section class="about-section">
      <h2>About RAISE Program</h2>
      <p>Founded in 2015, the RAISE (Research and Innovation for Sustainable Excellence) Program has grown from a small interdisciplinary initiative to a comprehensive research organization with over 200 affiliated researchers across 15 institutions worldwide. Our journey has been marked by groundbreaking discoveries, innovative solutions, and meaningful partnerships that have transformed industries and improved lives.</p>
      
      <p>What sets RAISE apart is our unique approach to problem-solving. We don't just bring together experts from different fields - we create integrated teams where biologists work side-by-side with computer scientists, where engineers collaborate with social scientists, and where theoretical research informs practical applications from day one. This approach has led to breakthroughs that traditional siloed research could never achieve.</p>
      
      <p>Our research facilities include state-of-the-art laboratories across three continents, supported by a robust digital infrastructure that enables seamless collaboration. We've invested over $50 million in cutting-edge equipment and technology, ensuring our researchers have the tools they need to push boundaries and explore new frontiers.</p>
      
      <p>The impact of our work can be seen in numerous sectors. Our sustainable agriculture innovations have helped smallholder farmers increase yields by 40% while reducing water usage. Our biomedical technologies are in clinical trials for treating previously incurable conditions. And our knowledge management systems are being adopted by major corporations to enhance productivity and innovation.</p>
    </section>

    <!-- Organizational Structure -->
    <section class="org-section">
      <h2>Organizational Structure</h2>
      <p>Our leadership team brings together diverse expertise from academia, industry, and government to drive our mission forward. This interdisciplinary approach ensures we consider all perspectives in our research and innovation strategies.</p>
      
      <div class="org-chart">
        <div class="org-level">
          <div class="org-item director">
            <img src="https://via.placeholder.com/150" alt="Dr. Elizabeth Parker" class="org-img">
            <h4>Program Director</h4>
            <p>Dr. Elizabeth Parker</p>
            <p>Professor of Sustainable Innovation, 15+ years research leadership</p>
          </div>
        </div>
        <div class="org-level">
          <div class="org-item project">
            <img src="https://via.placeholder.com/150" alt="Dr. Sarah Johnson" class="org-img">
            <h4>Research Division</h4>
            <p>Dr. Sarah Johnson</p>
            <p>Specializing in interdisciplinary research methodologies</p>
          </div>
          <div class="org-item project">
            <img src="https://via.placeholder.com/150" alt="Dr. Michael Chen" class="org-img">
            <h4>Innovation Division</h4>
            <p>Dr. Michael Chen</p>
            <p>Technology transfer and commercialization expert</p>
          </div>
          <div class="org-item project">
            <img src="https://via.placeholder.com/150" alt="Dr. Emily Rodriguez" class="org-img">
            <h4>Operations</h4>
            <p>Dr. Emily Rodriguez</p>
            <p>Strategic planning and partnership development</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Additional Content -->
    <section class="about-section">
      <h2>Our Research Approach</h2>
      <p>At RAISE, we've developed a unique four-phase research methodology that ensures both academic rigor and practical relevance:</p>
      
      <p><strong>1. Discovery:</strong> Our teams identify emerging challenges and opportunities through environmental scanning, stakeholder consultations, and foresight analysis. This phase often involves workshops with industry partners, community groups, and policymakers to ensure we're addressing real needs.</p>
      
      <p><strong>2. Exploration:</strong> We conduct interdisciplinary feasibility studies, combining theoretical research with small-scale practical experiments. This phase typically involves literature reviews, modeling, and proof-of-concept development across multiple disciplines simultaneously.</p>
      
      <p><strong>3. Development:</strong> Promising ideas move into full-scale development with dedicated teams and resources. We employ agile research methodologies, allowing for iterative improvements based on continuous feedback from end-users and stakeholders.</p>
      
      <p><strong>4. Implementation:</strong> Successful projects transition to real-world application through partnerships with industry, government, and NGOs. We measure impact through rigorous metrics and continue to refine solutions based on field data.</p>
      
      <p>This approach has allowed us to maintain an 80% success rate in translating research into practical applications, compared to the industry average of 30-40%. Our secret lies in the integration of diverse perspectives at every stage, ensuring solutions are technically sound, socially acceptable, and economically viable.</p>
    </section>
  </div>

  <footer>
    <div class="container">
      <div class="footer-content">
        <div class="footer-column">
          <h3>RAISE Program</h3>
          <ul>
            <li><a href="#">About Us</a></li>
            <li><a href="#">Our Mission</a></li>
            <li><a href="#">Leadership</a></li>
            <li><a href="#">Careers</a></li>
          </ul>
        </div>
        <div class="footer-column">
          <h3>Research</h3>
          <ul>
            <li><a href="project1.html">Project 1: ABH</a></li>
            <li><a href="project2.html">Project 2: IPTM</a></li>
            <li><a href="project3.html">Project 3: ATBI</a></li>
            <li><a href="project4.html">Project 4: Knowledge Management</a></li>
          </ul>
        </div>
        <div class="footer-column">
          <h3>Connect</h3>
          <ul>
            <li><a href="#">Contact Us</a></li>
            <li><a href="#">Newsletter</a></li>
            <li><a href="#">Events</a></li>
            <li><a href="#">Social Media</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; <span id="current-year"></span> RAISE Program. All rights reserved.</p>
      </div>
    </div>
  </footer>

  <script>
    // Set current year in footer
    document.getElementById('current-year').textContent = new Date().getFullYear();

    // Sliding hero animation with background images
    const heroSlides = document.querySelectorAll('.hero-slide');
    let currentSlide = 0;
    
    function showNextSlide() {
      heroSlides[currentSlide].classList.remove('active');
      currentSlide = (currentSlide + 1) % heroSlides.length;
      heroSlides[currentSlide].classList.add('active');
    }
    
    // Change slide every 5 seconds
    setInterval(showNextSlide, 5000);
    
    // Initialize first slide
    heroSlides[0].classList.add('active');

    // Scroll animation for all elements
    const animateOnScroll = () => {
      const elements = document.querySelectorAll('.mv-card, .org-item, .about-section, .org-section');
      const windowHeight = window.innerHeight;
      
      elements.forEach(element => {
        const elementPosition = element.getBoundingClientRect().top;
        const elementVisible = 150;
        
        if (elementPosition < windowHeight - elementVisible) {
          element.classList.add('visible');
        }
      });
    };

    // Add scroll event listener
    window.addEventListener('scroll', animateOnScroll);
    
    // Run once on page load
    animateOnScroll();

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
          behavior: 'smooth'
        });
      });
    });

    // Parallax effect for hero section
    window.addEventListener('scroll', function() {
      const slidingHero = document.querySelector('.sliding-hero');
      const scrollPosition = window.pageYOffset;
      slidingHero.style.backgroundPositionY = scrollPosition * 0.5 + 'px';
    });

    // Highlight cards on hover with animation
    const cards = document.querySelectorAll('.mv-card, .org-item');
    cards.forEach(card => {
      card.addEventListener('mouseenter', () => {
        card.style.transform = 'translateY(-10px)';
        card.style.boxShadow = '0 15px 30px rgba(0,0,0,0.2)';
      });
      
      card.addEventListener('mouseleave', () => {
        card.style.transform = '';
        card.style.boxShadow = '';
      });
    });
  </script>
</body>
</html>