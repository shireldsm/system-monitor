#!/usr/bin/env python3
"""
Script de monitoring système
Surveille CPU, RAM, disque et génère un rapport HTML
Auteur: Shirel Desmelliers
Date: Janvier 2026
"""

import psutil
import datetime
import os

# Seuils d'alerte (en pourcentage)
SEUIL_CPU = 80
SEUIL_RAM = 85
SEUIL_DISQUE = 90

def get_cpu_info():
    """Récupère les informations CPU"""
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count()
    return {
        'usage': cpu_percent,
        'cores': cpu_count,
        'alert': cpu_percent > SEUIL_CPU
    }

def get_ram_info():
    """Récupère les informations RAM"""
    ram = psutil.virtual_memory()
    return {
        'total': ram.total / (1024**3),  # Conversion en GB
        'used': ram.used / (1024**3),
        'percent': ram.percent,
        'alert': ram.percent > SEUIL_RAM
    }

def get_disk_info():
    """Récupère les informations disque"""
    disk = psutil.disk_usage('/')
    return {
        'total': disk.total / (1024**3),  # Conversion en GB
        'used': disk.used / (1024**3),
        'free': disk.free / (1024**3),
        'percent': disk.percent,
        'alert': disk.percent > SEUIL_DISQUE
    }

def get_network_info():
    """Récupère les informations réseau"""
    net = psutil.net_io_counters()
    return {
        'bytes_sent': net.bytes_sent / (1024**2),  # Conversion en MB
        'bytes_recv': net.bytes_recv / (1024**2)
    }

def generate_html_report(cpu, ram, disk, network):
    """Génère un rapport HTML avec les statistiques"""
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Fonction pour déterminer la couleur selon l'alerte
    def get_color(is_alert):
        return "#e74c3c" if is_alert else "#2ecc71"
    
    html = f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Rapport de Monitoring Système</title>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                max-width: 900px;
                margin: 40px auto;
                padding: 20px;
                background-color: #f5f5f5;
            }}
            .header {{
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 30px;
                border-radius: 10px;
                margin-bottom: 30px;
                text-align: center;
            }}
            .card {{
                background: white;
                padding: 25px;
                margin: 20px 0;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }}
            .metric {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 15px;
                margin: 10px 0;
                background: #f8f9fa;
                border-radius: 5px;
                border-left: 4px solid #667eea;
            }}
            .alert {{
                border-left-color: #e74c3c !important;
                background: #ffe5e5;
            }}
            .value {{
                font-size: 24px;
                font-weight: bold;
            }}
            .progress-bar {{
                width: 100%;
                height: 25px;
                background: #e0e0e0;
                border-radius: 12px;
                overflow: hidden;
                margin-top: 10px;
            }}
            .progress-fill {{
                height: 100%;
                transition: width 0.3s;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                font-weight: bold;
            }}
            .timestamp {{
                text-align: center;
                color: #666;
                margin-top: 30px;
            }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>📊 Rapport de Monitoring Système</h1>
            <p>Surveillance en temps réel de votre Mac</p>
        </div>
        
        <div class="card">
            <h2>🖥️ Processeur (CPU)</h2>
            <div class="metric {'alert' if cpu['alert'] else ''}">
                <span>Utilisation CPU</span>
                <span class="value">{cpu['usage']:.1f}%</span>
            </div>
            <div class="progress-bar">
                <div class="progress-fill" style="width: {cpu['usage']}%; background-color: {get_color(cpu['alert'])}">
                    {cpu['usage']:.1f}%
                </div>
            </div>
            <p style="margin-top: 10px; color: #666;">Nombre de cœurs : {cpu['cores']}</p>
        </div>
        
        <div class="card">
            <h2>💾 Mémoire RAM</h2>
            <div class="metric {'alert' if ram['alert'] else ''}">
                <span>Utilisation RAM</span>
                <span class="value">{ram['percent']:.1f}%</span>
            </div>
            <div class="progress-bar">
                <div class="progress-fill" style="width: {ram['percent']}%; background-color: {get_color(ram['alert'])}">
                    {ram['percent']:.1f}%
                </div>
            </div>
            <p style="margin-top: 10px; color: #666;">
                Utilisée : {ram['used']:.2f} GB / Total : {ram['total']:.2f} GB
            </p>
        </div>
        
        <div class="card">
            <h2>💿 Disque Dur</h2>
            <div class="metric {'alert' if disk['alert'] else ''}">
                <span>Utilisation Disque</span>
                <span class="value">{disk['percent']:.1f}%</span>
            </div>
            <div class="progress-bar">
                <div class="progress-fill" style="width: {disk['percent']}%; background-color: {get_color(disk['alert'])}">
                    {disk['percent']:.1f}%
                </div>
            </div>
            <p style="margin-top: 10px; color: #666;">
                Utilisé : {disk['used']:.2f} GB / Libre : {disk['free']:.2f} GB / Total : {disk['total']:.2f} GB
            </p>
        </div>
        
        <div class="card">
            <h2>🌐 Réseau</h2>
            <div class="metric">
                <span>Données envoyées</span>
                <span class="value">{network['bytes_sent']:.2f} MB</span>
            </div>
            <div class="metric">
                <span>Données reçues</span>
                <span class="value">{network['bytes_recv']:.2f} MB</span>
            </div>
        </div>
        
        <div class="timestamp">
            <p>Rapport généré le {timestamp}</p>
        </div>
    </body>
    </html>
    """
    
    return html

def main():
    """Fonction principale"""
    print("🔍 Analyse du système en cours...")
    
    # Collecte des informations
    cpu_info = get_cpu_info()
    ram_info = get_ram_info()
    disk_info = get_disk_info()
    network_info = get_network_info()
    
    # Affichage dans le terminal
    print(f"\n📊 Résultats:")
    print(f"CPU: {cpu_info['usage']:.1f}% {'⚠️ ALERTE' if cpu_info['alert'] else '✅'}")
    print(f"RAM: {ram_info['percent']:.1f}% {'⚠️ ALERTE' if ram_info['alert'] else '✅'}")
    print(f"Disque: {disk_info['percent']:.1f}% {'⚠️ ALERTE' if disk_info['alert'] else '✅'}")
    
    # Génération du rapport HTML
    html_content = generate_html_report(cpu_info, ram_info, disk_info, network_info)
    
    # Sauvegarde du fichier
    filename = f"system_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"\n✅ Rapport généré : {filename}")
    print(f"📂 Ouvrez le fichier dans votre navigateur pour voir le rapport complet")

if __name__ == "__main__":
    main()