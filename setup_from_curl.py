#!/usr/bin/env python3
"""
Convert cURL command to ytmusicapi headers format
"""

import json
import re

def extract_headers_from_curl():
    """Extract headers from the cURL command and create headers_auth.json"""
    
    # The cURL command from the user
    curl_command = """curl 'https://music.youtube.com/youtubei/v1/music/get_search_suggestions?prettyPrint=false' \\
  -H 'accept: */*' \\
  -H 'accept-language: en-US,en;q=0.9' \\
  -H 'authorization: SAPISIDHASH 1753138392_4ec8f315e762216d5b9bcf9c8c3de38ad7f38e85_u SAPISID1PHASH 1753138392_4ec8f315e762216d5b9bcf9c8c3de38ad7f38e85_u SAPISID3PHASH 1753138392_4ec8f315e762216d5b9bcf9c8c3de38ad7f38e85_u' \\
  -H 'content-type: application/json' \\
  -b 'LOGIN_INFO=AFmmF2swRQIgNeF2SjDChLOaIZv-gu6S0so2Ek-O-jjnVQ8Ox9q-MXcCIQDJ-s00hsqf4aCjn3tDIslYSb3e0n_RjMALj4ZmwHEPhA:QUQ3MjNmeVNGVy0wbTZ0c210endrUEpuUUh0YXBUVThBbll5YV9KXzZ5TENwQmtORGdkbVlWcGRqT2tZM2NNb0psaWdFeDFYX1VTeHU3R0dIbUV2MjJqUzU5WS03Rm1sNVZzTk1EODhOQTZoWHpfUnlZaElnUjF6ckRjZ3FGWU1yOWVwWUlpbTFPbkFkaGZPVkN1RGFYdl9kdkpUMGNkQUZR; __Secure-YEC=Cgt3S0lGTEdiZU1Uayix_fS_BjInCgJESxIhEh0SGwsMDg8QERITFBUWFxgZGhscHR4fICEiIyQlJiAq; VISITOR_INFO1_LIVE=U_S18jGszsQ; VISITOR_PRIVACY_METADATA=CgJVUxIEGgAgHg%3D%3D; HSID=AxEqONJyv3USIK3xW; SSID=A9N7rYotz3KpIV0Ax; APISID=AmeH3WOnBozF970W/AF9avXezqPHCcsOSc; SAPISID=LsOsV-mEy_Rcykri/AXBFC4LjL0p3mrsUY; __Secure-1PAPISID=LsOsV-mEy_Rcykri/AXBFC4LjL0p3mrsUY; __Secure-3PAPISID=LsOsV-mEy_Rcykri/AXBFC4LjL0p3mrsUY; PREF=f6=40000080&repeat=NONE&f4=4000000&tz=America.Chicago&f7=100&volume=4; SID=g.a000ywihg-CVgdrvLYdnGjr681cUO3cGIrSxCpRiyCQD4OKKoDohcaLl8skmykwt_tyaJJOGjQACgYKAd0SARMSFQHGX2Mio2QwyQ8YPHR88D6xT9dRtxoVAUF8yKqFDZ48kFBKRB8hGKkXjCZO0076; __Secure-1PSID=g.a000ywihg-CVgdrvLYdnGjr681cUO3cGIrSxCpRiyCQD4OKKoDohsyc-SewNc3qvqCABwvv3KgACgYKAfcSARMSFQHGX2Mi3_sTqt4GSnsIvd0to7XJXhoVAUF8yKpbss74LPg3azZQD-Sk32od0076; __Secure-3PSID=g.a000ywihg-CVgdrvLYdnGjr681cUO3cGIrSxCpRiyCQD4OKKoDoh0YCaTG5RdQX10lJ1ZGbJ5AACgYKAfoSARMSFQHGX2Mi-r6C88nAyI0Qw37-NVXMkxoVAUF8yKpM4uqF5ZmtZLxFl6BPtXvJ0076; YSC=odIoqE-tx20; __Secure-1PSIDTS=sidts-CjEB5H03P0aJO4ZKseU0_jfeYLwd-qL6-JGBd3XpzkwhHlCOqtZjqMT7WCY-wmRIuTm3EAA; __Secure-3PSIDTS=sidts-CjEB5H03P0aJO4ZKseU0_jfeYLwd-qL6-JGBd3XpzkwhHlCOqtZjqMT7WCY-wmRIuTm3EAA; __Secure-ROLLOUT_TOKEN=COm6ua_G1MDEFxDvhPWt_9eMAxjxucKsyM6OAw%3D%3D; _gcl_au=1.1.1936549529.1753137816; SIDCC=AKEyXzW1xYXd9Ft2reAzQ6HHgNisolO63oLJEdZ_96sd5E9OzchAyLkWZixkLxq5TEUBDoNP9w; __Secure-1PSIDCC=AKEyXzU3iTK_wK4zHFzGiTLvwH3IMRIOEKk-g2bvjv7eX-65f2WGRDFA2qXIVh3KJpRtrziIdg; __Secure-3PSIDCC=AKEyXzX8LqtAqdMgv-eeHJuxfiSeVekzSqKrshXSyfLE03D1KcS3skVKfHrIvlrjgCP6Q2TqOQ' \\
  -H 'origin: https://music.youtube.com' \\
  -H 'priority: u=1, i' \\
  -H 'referer: https://music.youtube.com/playlist?list=PLSJIexHLewq1RbGrsjIbKDwdazJCZGz07' \\
  -H 'sec-ch-ua: "Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"' \\
  -H 'sec-ch-ua-arch: "arm"' \\
  -H 'sec-ch-ua-bitness: "64"' \\
  -H 'sec-ch-ua-form-factors: "Desktop"' \\
  -H 'sec-ch-ua-full-version: "138.0.7204.158"' \\
  -H 'sec-ch-ua-full-version-list: "Not)A;Brand";v="8.0.0.0", "Chromium";v="138.0.7204.158", "Google Chrome";v="138.0.7204.158"' \\
  -H 'sec-ch-ua-mobile: ?0' \\
  -H 'sec-ch-ua-model: ""' \\
  -H 'sec-ch-ua-platform: "macOS"' \\
  -H 'sec-ch-ua-platform-version: "14.6.1"' \\
  -H 'sec-ch-ua-wow64: ?0' \\
  -H 'sec-fetch-dest: empty' \\
  -H 'sec-fetch-mode: same-origin' \\
  -H 'sec-fetch-site: same-origin' \\
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36' \\
  -H 'x-browser-copyright: Copyright 2025 Google LLC. All rights reserved.' \\
  -H 'x-browser-validation: qvLgIVtG4U8GgiRPSI9IJ22mUlI=' \\
  -H 'x-browser-year: 2025' \\
  -H 'x-client-data: CK21yQEIibbJAQiktskBCKmdygEIyf/KAQiTocsBCKOjywEIhqDNAQj+pc4BCNzWzgEI3/vOAQin/M4BCOj8zgEIhv3OAQiJ/c4BCLn9zgEYy/rOARjQ+s4BGL/7zgE=' \\
  -H 'x-goog-authuser: 0' \\
  -H 'x-goog-visitor-id: CgtVX1MxOGpHc3pzUSjXifvDBjIKCgJVUxIEGgAgHg%3D%3D' \\
  -H 'x-origin: https://music.youtube.com' \\
  -H 'x-youtube-bootstrap-logged-in: true' \\
  -H 'x-youtube-client-name: 67' \\
  -H 'x-youtube-client-version: 1.20250716.03.00'"""
    
    # Extract headers and cookies
    headers = {}
    cookies = {}
    
    # Extract -H headers
    header_pattern = r"-H '([^:]+):\s*([^']+)'"
    header_matches = re.findall(header_pattern, curl_command)
    
    for key, value in header_matches:
        headers[key] = value.strip()
    
    # Extract cookies from -b
    cookie_pattern = r"-b '([^']+)'"
    cookie_match = re.search(cookie_pattern, curl_command)
    
    if cookie_match:
        cookie_string = cookie_match.group(1)
        # Parse cookies
        for cookie in cookie_string.split('; '):
            if '=' in cookie:
                key, value = cookie.split('=', 1)
                cookies[key] = value
    
    # Add cookies to headers
    if cookies:
        headers['cookie'] = '; '.join([f"{k}={v}" for k, v in cookies.items()])
    
    # Create the headers file format for ytmusicapi
    auth_data = {
        "Accept": headers.get('accept', '*/*'),
        "Accept-Language": headers.get('accept-language', 'en-US,en;q=0.9'),
        "Authorization": headers.get('authorization', ''),
        "Content-Type": headers.get('content-type', 'application/json'),
        "Cookie": headers.get('cookie', ''),
        "Origin": headers.get('origin', 'https://music.youtube.com'),
        "Referer": headers.get('referer', 'https://music.youtube.com/'),
        "User-Agent": headers.get('user-agent', ''),
        "X-Goog-AuthUser": headers.get('x-goog-authuser', '0'),
        "X-Goog-Visitor-Id": headers.get('x-goog-visitor-id', ''),
        "X-YouTube-Client-Name": headers.get('x-youtube-client-name', '67'),
        "X-YouTube-Client-Version": headers.get('x-youtube-client-version', ''),
    }
    
    # Write to file
    with open('headers_auth.json', 'w') as f:
        json.dump(auth_data, f, indent=2)
    
    print("✅ Successfully created headers_auth.json")
    print("🎵 You can now search your playlists!")
    
    return auth_data

if __name__ == "__main__":
    extract_headers_from_curl() 