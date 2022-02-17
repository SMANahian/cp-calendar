from flask import Blueprint, make_response, request

from const import RESOURCES
from ical_setup import load_contests_per_need

calendar_routes_blueprint = Blueprint("calendar_routes", __name__)



@calendar_routes_blueprint.route('/', methods=['GET'])
def calendar():
    resources_id = request.args.getlist('resource')
    resources = {}
    if len(resources_id) == 0:
        resources = RESOURCES
    else:
        for resource_id in resources_id:
            allowed = request.args.get(str(resource_id)+"_a").split()
            restricted = request.args.get(str(resource_id)+"_r").split()
            resources[int(resource_id)] = (allowed, restricted)
        
        gl_a = request.args.get('gl_a').split()
        gl_r = request.args.get('gl_r').split()
        resources["global"] = (gl_a, gl_r)
    print(resources)
    s = load_contests_per_need(resources)
    response = make_response(s)
    response.headers["Content-Disposition"] = "attachment; filename=calendar.ics"
    return response