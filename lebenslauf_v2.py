# V2 - Updated CV with QA/Software Testing focus

import webbrowser
import os
from playwright.sync_api import sync_playwright

html_content = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 40px;
            color: #333;
        }
        
        .container {
            display: grid;
            grid-template-columns: 65% 35%;
            gap: 20px;
            max-width: 1000px;
            margin: 0 auto;
        }
        
        h1 {
            font-size: 36px;
            color: #2c3e50;
            margin: 0 0 20px 0;
        }
        
        .contact-info {
            margin-bottom: 30px;
            line-height: 1.8;
        }
        
        .contact-info p {
            margin: 5px 0;
        }
        
        h2 {
            color: #3498db;
            font-size: 18px;
            margin: 30px 0 15px 0;
            border-bottom: 1px solid #3498db;
            padding-bottom: 5px;
        }
        
        .job {
            margin-bottom: 30px;
        }
        
        .company-name {
            font-weight: bold;
            font-size: 16px;
            margin-bottom: 5px;
        }
        
        .company-location {
            color: #666;
            font-size: 14px;
            margin-bottom: 5px;
        }
        
        .job-details {
            color: #333;
            margin-bottom: 10px;
        }
        
        .job-description {
            margin-top: 10px;
            line-height: 1.6;
        }
        
        .job-description ul {
            margin: 10px 0;
            padding-left: 20px;
        }
        
        .job-description li {
            margin-bottom: 8px;
            line-height: 1.5;
        }

        .sidebar {
            padding-left: 15px;
            padding-right: 15px;
            border-left: 1px solid #e0e0e0;
        }
        
        .sidebar h2 {
            color: #3498db;
            font-size: 18px;
            margin: 30px 0 15px 0;
            border-bottom: 1px solid #3498db;
            padding-bottom: 5px;
        }

        .sidebar h2:first-of-type {
            margin-top: 0;
        }
        
        .profile-image {
            width: 100%;
            height: auto;
            margin-bottom: 20px;
            display: block;
        }

        @media print {
            body {
                padding: 20px;
            }
            .sidebar {
                border-left: 1px solid #e0e0e0 !important;
                -webkit-print-color-adjust: exact;
            }
        }
        
        .kenntnisse-list {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        
        .kenntnisse-list li {
            color: #333;
            margin-bottom: 10px;
            padding-left: 20px;
            position: relative;
            word-wrap: break-word;
            hyphens: auto;
        }
        
        .kenntnisse-list li::before {
            content: "•";
            color: #3498db;
            position: absolute;
            left: 0;
            top: 0;
        }
        
        .section-title {
            color: #3498db;
            font-size: 20px;
            border-bottom: 1px solid #3498db;
            padding-bottom: 5px;
            margin: 25px 0 15px 0;
        }
        
        .education-item {
            margin-bottom: 25px;
        }
        
        .university {
            font-weight: bold;
            margin-bottom: 5px;
        }
        
        .education-details p {
            margin: 5px 0;
        }
        
        .language-item {
            margin-bottom: 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .language-name {
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .competency-section {
            margin-bottom: 20px;
        }
        
        .competency-title {
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 8px;
            font-size: 14px;
        }
        
        .competency-items {
            color: #666;
            line-height: 1.6;
            font-size: 13px;
        }
        
        .job-separator {
            color: #3498db;
            font-size: 18px;
            margin-right: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="main-content">
            <h1>Husameldin Osman</h1>
            <div class="contact-info">
                <p>📍 Adresse: Engelmannweg 71, 13403 Berlin</p>
                <p>✉️ E-Mail: hossamossman92@gmail.com</p>
                <p>📞 Mobil: +49 (0)157 5163 7357</p>
                <p>📅 Geburtsdatum: 10. Oktober 1992</p>
            </div>

            <h2>BERUFLICHE LAUFBAHN</h2>
            <div class="job">
                <p class="company-name"><span class="job-separator">🔹</span>Software & Support Media GmbH</p>
                <p class="company-location">Berlin</p>
                <p class="job-details">📆 seit 2023</p>
                <p class="job-details"><strong>Werkstudent QA / Software Testing (Wirtschaftsinformatik)</strong></p>
                <div class="job-description">
                    <ul>
                        <li>Manuelles und automatisiertes Testing von Web-Plattformen und digitalen Produkten</li>
                        <li>API-Testing mit GraphQL (Validierung von Queries, Mutations, Response-Strukturen)</li>
                        <li>Testautomatisierung mit Cypress</li>
                        <li>Erstellung strukturierter Testfälle und Testpläne</li>
                        <li>Durchführung von Edge-Case- und Negativtests</li>
                        <li>Validierung von Subscription- und Payment-Flows</li>
                        <li>Analyse und Dokumentation von Bugs in YouTrack</li>
                        <li>Backend-Datenprüfung (JSON-Strukturen, Schema-Validierung)</li>
                        <li>Testing von AI/RAG-Systemen (Retrieval-Logik, Chunking, Prompt-Validierung)</li>
                        <li>Enge Zusammenarbeit mit Entwicklern zur Fehleranalyse und Qualitätssicherung</li>
                        <li>Unterstützung bei Release-Tests und Qualitätssicherung vor Deployments</li>
                    </ul>
                </div>
            </div>

            <div class="job">
                <p class="company-name"><span class="job-separator">🔹</span>Natural Cover Multi Service</p>
                <p class="job-details">📆 Februar 2018 – 2019</p>
                <p class="job-details"><strong>Manager of Sales</strong></p>
                <div class="job-description">
                    <ul>
                        <li>Entwicklung und Umsetzung von Vertriebsstrategien</li>
                        <li>Kundenakquise und CRM-Verwaltung</li>
                        <li>Koordination des Verkaufsteams</li>
                        <li>Prozessoptimierung zur Umsatzsteigerung</li>
                    </ul>
                </div>
            </div>

            <div class="job">
                <p class="company-name"><span class="job-separator">🔹</span>Alinjaz Sudanese German Specialized Hospital</p>
                <p class="job-details">📆 Mai 2014 – Januar 2018</p>
                <p class="job-details"><strong>Supportmanager</strong></p>
                <div class="job-description">
                    <ul>
                        <li>Koordination von externen Dienstleistern</li>
                        <li>Qualitätsprüfung und Kostenanalyse</li>
                        <li>Lieferantenkommunikation und Budgetplanung</li>
                    </ul>
                </div>
            </div>

            <h2>AUSBILDUNG</h2>
            <div class="education-item">
                <p class="university">Technische Hochschule Brandenburg</p>
                <div class="education-details">
                    <p>📆 März 2022 - Januar 2025</p>
                    <p>🎓 Master in Wirtschaftsinformatik</p>
                    <p><strong>Masterarbeit:</strong> Integration von Künstlicher Intelligenz in CRM-Systeme (Salesforce)</p>
                </div>
            </div>

            <div class="education-item">
                <p class="university">The National Ribat University</p>
                <div class="education-details">
                    <p>📆 2009 - 2013</p>
                    <p>🎓 Bachelor in Business Administration (BBA)</p>
                </div>
            </div>
        </div>
        
        <div class="sidebar">
            <img src="pf.jpeg" alt="Profilbild" class="profile-image">
            
            <h2 class="section-title">TECHNISCHE KOMPETENZEN</h2>
            
            <div class="competency-section">
                <div class="competency-title">Testing & QA</div>
                <div class="competency-items">Manual Testing • Test Design • Edge Case Testing • Regression Testing • Release Testing</div>
            </div>
            
            <div class="competency-section">
                <div class="competency-title">Automation & APIs</div>
                <div class="competency-items">Cypress • GraphQL • Postman • Insomnia</div>
            </div>
            
            <div class="competency-section">
                <div class="competency-title">Tools & Technologien</div>
                <div class="competency-items">YouTrack • Git • JSON • WordPress • Salesforce • Slack</div>
            </div>

            <h2 class="section-title">SPRACHEN</h2>
            <div class="language-item">
                <div class="language-name">🇩🇪 Deutsch</div>
                <div>Fließend (C1)</div>
            </div>
            <div class="language-item">
                <div class="language-name">🇬🇧 Englisch</div>
                <div>Fließend (C1)</div>
            </div>
            <div class="language-item">
                <div class="language-name">🇸🇩 Arabisch</div>
                <div>Muttersprache</div>
            </div>

            <h2 class="section-title">ZERTIFIZIERUNGEN</h2>
            <ul class="kenntnisse-list">
                <li>🏅 SQL-Zertifizierung</li>
                <li>🏅 Salesforce Development</li>
                <li>🏅 SAP S/4HANA (TS410)</li>
                <li>🏅 SAP SD – Auftragsabwicklung</li>
                <li>🏅 SAP S/4HANA Customizing</li>
                <li>🏅 WordPress</li>
                <li>🏅 SEA</li>
                <li>🏅 YOAST WordPress SEO</li>
            </ul>
        </div>
    </div>
</body>
</html>
"""

# HTML temporär speichern
with open('lebenslauf_v2.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

# PDF erstellen
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('file://' + os.path.realpath('lebenslauf_v2.html'))
    page.pdf(path="Lebenslauf_Husameldin_Osman_V2.pdf", format="A4")
    browser.close()

# Temporäre HTML-Datei löschen
os.remove('lebenslauf_v2.html')
