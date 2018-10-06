from app import api
from app.auth import login_required


@api.route("/accesswithtoken")
@login_required
def accesswithtoken():
    return "Im Login Required!"
