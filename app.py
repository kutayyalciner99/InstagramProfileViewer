from flask import Flask, request, jsonify
import instaloader

app = Flask(__name__)


@app.route("/instagram-profile", methods=["POST"])
def get_instagram_profile():
    username = request.json["username"]
    ig = instaloader.Instaloader()

    try:
        profile = instaloader.Profile.from_username(ig.context, username)

        response = {
            "username": profile.username,
            "media_count": profile.mediacount,
            "followers": profile.followers,
            "followees": profile.followees,
            "bio": profile.biography,
            "profile_pic_url": profile.profile_pic_url,
        }

        return jsonify(response), 200, {"Content-Type": "application/json"}

    except instaloader.exceptions.ProfileNotExistsException:
        return (
            jsonify({"error": "Profile not found"}),
            404,
            {"Content-Type": "application/json"},
        )


if __name__ == "__main__":
    app.run()
