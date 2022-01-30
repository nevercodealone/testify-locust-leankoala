from locust import HttpUser, task, between

def auth(self):
    response = self.client.post("/secure_area/login_check", json={"_csrf_token":"Pznw0aM2ElSEj4Tvfr26g-2kBsROT7GdghjdL71k8RE", "_username": "nevercodealone", "_password": "xCFu_4GbZjFoAs", "_submit":"Log in"}, catch_response=True)
    cookie = response.cookies.get('set-cookie')
    print(response.status_code)
    return cookie

class Current(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        self.cookie = auth(self)

    @task
    def current(self):
        with self.client.get("/rest/projects/current/", json={"cookie": "_ga=GA1.2.1886205441.1643472377; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; __tawkuuid=e::monitor.leankoala.com::tQGEpaFmtpjtGmK6RP9FdzS0vbGcnlw/HUz3eKCiiotpeXFJe4PFzBhvb45RfgHe::2; TawkConnectionTime=0; PHPSESSID=" + str(self.cookie) + "; REMEMBERME=S29hbGFtb25cSW5jaWRlbnREYXNoYm9hcmRCdW5kbGVcRW50aXR5XFVzZXI6Ym1WMlpYSmpiMlJsWVd4dmJtVT06MTY0NDE3MDkwNTpmZmI4MmRlMGQ5Yzc3N2U3YWU2YzRkNGM5YzU1NTY4ZDdlMjg5ZWQxYmQwNTFhNWVkYzJmZDNiNzk4ZDZiNGVi"}, catch_response=True) as response:
            print(response.status_code)
            if response.status_code != 200:
                response.failure("Wrong resonse code for current route: " + str(response.status_code))
