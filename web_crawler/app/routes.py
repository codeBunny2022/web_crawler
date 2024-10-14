from flask import Blueprint, request, jsonify
from .crawler import crawl

main = Blueprint('main', __name__)

@main.route('/crawl', methods=['POST'])
def crawl_web():
    data = request.get_json()
    root_url = data.get('root_url')
    depth = data.get('depth')
    if not root_url or depth is None:
        return jsonify({"error": "Invalid input"}), 400
    crawled_links = crawl(root_url, depth)
    return jsonify({
        "root_url": root_url,
        "depth": depth,
        "crawled_links": crawled_links
    })
