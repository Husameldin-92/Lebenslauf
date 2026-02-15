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
        
        .job-title {
            font-weight: bold;
            font-size: 18px;
            color: #2c3e50;
            margin-bottom: 8px;
            margin-top: 0;
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
        
        .profile-summary {
            font-style: italic;
            color: #555;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 1px solid #e0e0e0;
            line-height: 1.6;
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
                <p>📍 Isländische Straße 12, 13409 Berlin</p>
                <p>✉️ hossamossman92@gmail.com</p>
                <p>📞 +49 157 5163 7357</p>
                <p>📅 10. Oktober 1992</p>
            </div>

            <h2>BERUFSERFAHRUNG</h2>
            <div class="job">
                <p class="job-title">QA Engineer / Software Tester</p>
                <p class="company-name"><span class="job-separator">🔹</span>Software & Support Media GmbH – Berlin</p>
                <p class="job-details">📆 seit 2023</p>
                <p class="profile-summary">Schwerpunkt: Frontend- und Backend-Systeme, API-Validierung und Testautomatisierung in komplexen Web- und Mobile-Umgebungen</p>
                <div class="job-description">
                    <ul>
                        <li>Manuelles und automatisiertes Testing von Web-Anwendungen</li>
                        <li>Testing nativer iOS- und Android-Apps</li>
                        <li>API-Testing mit GraphQL (Validierung von Queries, Mutations und Response-Strukturen)</li>
                        <li>Backend-Datenprüfung und Schema-Validierung (JSON)</li>
                        <li>Testing von AI/RAG-Systemen (Retrieval-Logik, Chunking, Prompt-Validierung)</li>
                        <li>Entwicklung und Pflege von Testautomatisierung mit Cypress</li>
                        <li>Erstellung strukturierter Testfälle und Testpläne</li>
                        <li>Durchführung von Regression-, Edge-Case- und Negativtests</li>
                        <li>Validierung komplexer Subscription- und Payment-Flows</li>
                        <li>Identifikation, Reproduktion und präzise Dokumentation reproduzierbarer Softwarefehler</li>
                        <li>Enge Zusammenarbeit mit Entwicklern zur Fehleranalyse und Qualitätssicherung</li>
                        <li>Unterstützung bei Release-Tests vor Deployments</li>
                    </ul>
                </div>
            </div>

            <div class="job">
                <p class="company-name"><span class="job-separator">🔹</span>Manager of Sales</p>
                <p class="company-location">Natural Cover Multi Service</p>
                <p class="job-details">📆 Februar 2018 – 2019</p>
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
                <p class="company-name"><span class="job-separator">🔹</span>Supportmanager</p>
                <p class="company-location">Alinjaz Sudanese German Specialized Hospital</p>
                <p class="job-details">📆 Mai 2014 – Januar 2018</p>
                <div class="job-description">
                    <ul>
                        <li>Koordination externer Dienstleister</li>
                        <li>Qualitätsprüfung und Kostenanalyse</li>
                        <li>Lieferantenkommunikation und Budgetplanung</li>
                        <li>Vertrags- und Einkaufsverhandlungen</li>
                    </ul>
                </div>
            </div>

            <h2>AUSBILDUNG</h2>
            <div class="education-item">
                <p class="university">Master in Wirtschaftsinformatik</p>
                <div class="education-details">
                    <p>Technische Hochschule Brandenburg</p>
                    <p>📆 März 2022 – Januar 2025</p>
                    <p><strong>Masterarbeit:</strong></p>
                    <p>„Chancen und Herausforderungen der Integration von Künstlicher Intelligenz in den CRM-Bereich von ERP-Systemen – Das Beispiel Salesforce"</p>
                </div>
            </div>

            <div class="education-item">
                <p class="university">Bachelor of Business Administration (BBA)</p>
                <div class="education-details">
                    <p>The National Ribat University</p>
                    <p>📆 2009 – 2013</p>
                </div>
            </div>
        </div>
        
        <div class="sidebar">
            <img src="pf.jpeg" alt="Profilbild" class="profile-image">
            
            <h2 class="section-title">TECHNISCHE KOMPETENZEN</h2>
            
            <div class="competency-section">
                <div class="competency-title">Testing & QA</div>
                <div class="competency-items">Manual Testing • Regression Testing • Edge Case Testing • Release Testing • Mobile Testing</div>
            </div>
            
            <div class="competency-section">
                <div class="competency-title">Automation & APIs</div>
                <div class="competency-items">Cypress • GraphQL • Postman • Insomnia</div>
            </div>
            
            <div class="competency-section">
                <div class="competency-title">Mobile</div>
                <div class="competency-items">Native iOS Testing • Native Android Testing</div>
            </div>
            
            <div class="competency-section">
                <div class="competency-title">Tools & Technologien</div>
                <div class="competency-items">YouTrack • Git • JSON • WordPress • Salesforce • Slack</div>
            </div>

            <h2 class="section-title">SPRACHEN</h2>
            <div class="language-item">
                <div class="language-name">Deutsch</div>
                <div>– C1</div>
            </div>
            <div class="language-item">
                <div class="language-name">Englisch</div>
                <div>– C1</div>
            </div>
            <div class="language-item">
                <div class="language-name">Arabisch</div>
                <div>– Muttersprache</div>
            </div>

            <h2 class="section-title">ZERTIFIZIERUNGEN</h2>
            <ul class="kenntnisse-list">
                <li>SQL-Zertifizierung</li>
                <li>Salesforce Development</li>
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
