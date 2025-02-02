# Rebuilding the PDF without symbols and ensuring a clean layout

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
        
        .company {
            color: #3498db;
            text-decoration: none;
        }
        
        .period {
            color: #666;
            margin: 5px 0;
        }
        
        .job {
            margin-bottom: 30px;
        }
        
        .company-name {
            font-weight: bold;
            font-size: 16px;
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
        
        .job-title {
            font-weight: bold;
            margin: 0;
        }
        
        .profile-image {
            width: 200px;
            height: auto;
            float: right;
            margin-left: 20px;
            margin-bottom: 20px;
        }
        
        .skills-list {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        
        .skills-list li {
            margin-bottom: 8px;
            position: relative;
            padding-left: 15px;
        }
        
        .skills-list li:before {
            content: "•";
            color: #3498db;
            position: absolute;
            left: 0;
        }
        
        .language-grid {
            display: grid;
            grid-template-columns: auto 100px;
            gap: 5px;
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
        
        .skills-list {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        
        .skills-list li {
            margin-bottom: 8px;
            position: relative;
            padding-left: 15px;
            line-height: 1.4;
        }
        
        .skills-list li:before {
            content: "•";
            color: #3498db;
            position: absolute;
            left: 0;
        }
        
        .language-grid {
            display: grid;
            grid-template-columns: 1fr auto;
            gap: 10px;
            margin-bottom: 8px;
        }

        .language-grid div:nth-child(2n) {
            text-align: right;
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
        
        .sprachen-table {
            width: 100%;
            table-layout: fixed;
            border-spacing: 0;
            margin-bottom: 20px;
        }
        
        .sprachen-table td:first-child {
            width: 60%;
        }
        
        .sprachen-table td:last-child {
            width: 40%;
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
        
        .skills-tags {
            margin-top: 10px;
            color: #666;
            line-height: 1.6;
        }
        
        .skills-tags span {
            color: #3498db;
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
                <p class="job-details">📆 seit 2023 | Werkstudent (Wirtschaftsinformatik, Second-Line-Support)</p>
                <p class="job-description">Als Werkstudent im Second-Line-Support bin ich die Schnittstelle zwischen Marketing & Sales (First-Line-Support) und den Entwicklern (Third-Line-Support). Mein Wissen in Wirtschaftsinformatik, Marketing und Entwicklung hilft dabei, Prozesse zu optimieren, Probleme schneller zu lösen und die Arbeitslast der Entwickler zu reduzieren.</p>
                <p class="skills-tags">
                    <span>#Werkstudent</span> <span>#Salesforce</span> <span>#WordPress</span> <span>#Slack</span> <span>#YouTrack</span> <span>#Mailchimp</span> <span>#Redsys</span> <span>#ConfTool</span> <span>#Kommunikation</span>
                </p>
            </div>

            <div class="job">
                <p class="company-name"><span class="job-separator">🔹</span>Natural Cover Multi Service</p>
                <p class="job-details">📆 Februar 2018 - 2019 | Manager of Sales</p>
                <p class="job-description">Verantwortlich für Vertriebsstrategien, Kundenakquise und Geschäftsentwicklung. Koordination des Verkaufsteams und Optimierung interner Prozesse zur Umsatzsteigerung.</p>
                <p class="skills-tags">
                    <span>#Sales</span> <span>#CRM</span> <span>#Kundenakquise</span> <span>#Teamkoordination</span> <span>#Vertriebsoptimierung</span>
                </p>
            </div>

            <div class="job">
                <p class="company-name"><span class="job-separator">🔹</span>Alinjaz Sudanese German Specialized Hospital</p>
                <p class="job-details">📆 Mai 2014 - Januar 2018 | Supportmanager</p>
                <p class="job-description">Verantwortlich für die Kommunikation und Verhandlungen mit externen Unternehmen für den Einkauf und die Wartung medizinischer Ausrüstung. Koordination der internen Bedarfsplanung, Qualitätsbewertung, Kostenanalyse und Lieferplanung.</p>
                <p class="skills-tags">
                    <span>#Einkaufsmanagement</span> <span>#Lieferantenkommunikation</span> <span>#Qualitätsprüfung</span> <span>#Verhandlungsführung</span> <span>#Budgetplanung</span>
                </p>
            </div>

            <h2>AUSBILDUNG</h2>
            <div class="education-item">
                <p class="university">Technische Hochschule Brandenburg</p>
                <div class="education-details">
                    <p>📆 März 2022 - Januar 2025</p>
                    <p>🎓 Master in Wirtschaftsinformatik</p>
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
            
            <h2 class="section-title">KENNTNISSE</h2>
            <ul class="kenntnisse-list">
                <li>Salesforce-Administration</li>
                <li>WordPress</li>
                <li>BPMN 2.0</li>
                <li>SQL-Datenbankmanagement</li>
                <li>SAP S/4HANA</li>
                <li>Frontend-Entwicklung</li>
                <li>Kommunikation</li>
                <li>Microsoft Office</li>
            </ul>

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
with open('lebenslauf.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

# PDF erstellen
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('file://' + os.path.realpath('lebenslauf.html'))
    page.pdf(path="Lebenslauf_Husameldin_Osman.pdf", format="A4")
    browser.close()

# Temporäre HTML-Datei löschen
os.remove('lebenslauf.html')
