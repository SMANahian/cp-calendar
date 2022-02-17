import os
import json
from urllib.parse import urlparse
from flask import Flask, render_template, make_response, send_from_directory, request
from .calendar_routes import calendar_routes_blueprint

from .const import RESOURCES_JSON_FILE_PATH


def create_app():
    webapp = Flask(
        __name__,
        template_folder=os.path.join("front_end", "pages"),
        static_folder=os.path.join("front_end", "assets"),
    )

    webapp.register_blueprint(calendar_routes_blueprint, url_prefix='/calendar/')

    @webapp.route('/')
    @webapp.route('/home')
    @webapp.route('/home/')
    def main_home():
        data = None
        with open(RESOURCES_JSON_FILE_PATH, 'r') as f:
            data = json.load(f)
        return render_template("main/home.html", resources=data['objects'])

    @webapp.route("/sitemap")
    @webapp.route("/sitemap/")
    @webapp.route("/sitemap.xml")
    def sitemap():
        host_components = urlparse(request.host_url)
        host_base = (host_components.scheme if 1 == 2 else "https") + "://" + host_components.netloc

        static_urls = list()
        for rule in webapp.url_map.iter_rules():
            if not (
                str(rule).startswith("/fun")
                or str(rule).startswith("/sitemap")
                or str(rule).startswith("/favicon")
                or str(rule).startswith("/assets")
                or str(rule).startswith("/robots.txt")
                or str(rule).startswith("/google44423c6d3d4f861b.html")
            ):
                static_urls.append(
                    {
                        "loc": f"{host_base}{str(rule)}"
                    }
                )

        xml_sitemap = render_template(
            "public/sitemap.xml", 
            static_urls=static_urls
        )
        response = make_response(xml_sitemap)
        response.headers["Content-Type"] = "application/xml"

        return response


    @webapp.errorhandler(404)
    def page_not_found(error):
        return render_template("main/404.html"), 404


    @webapp.route("/favicon")
    @webapp.route("/favicon/")
    @webapp.route("/favicon.ico")
    def favicon():
        return send_from_directory(
            os.path.join(webapp.root_path, 'front_end', 'assets', 'images'),
            'favicon.ico',
            mimetype='image/vnd.microsoft.icon'
        )
    
    @webapp.route("/robots.txt")
    def robot_txt_file():
        return send_from_directory(
            os.path.join(webapp.root_path, 'front_end', 'pages', 'public'),
            'robots.txt',
            mimetype='text/txt'
        )

    @webapp.route("/google44423c6d3d4f861b.html")
    def google_site_verification():
        return render_template("public/google_site_verification.html")


    return webapp
