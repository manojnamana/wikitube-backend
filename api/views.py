from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from youtube_transcript_api import YouTubeTranscriptApi

@require_http_methods(["GET", "OPTIONS"])
def get_subtitles(request):
    # Handle OPTIONS request (preflight for CORS)
    if request.method == "OPTIONS":
        response = JsonResponse({"status": "OK"})
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type"
        return response

    # Extract the videoId from the query parameters
    video_id = request.GET.get('videoId')

    if not video_id:
        return JsonResponse({"error": "Invalid or missing videoId"}, status=400)

    try:
        # Fetch the captions (subtitles) for the video
        captions = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        return JsonResponse({"captions": captions}, status=200)
    except Exception as e:
        # Log the error and return an error response
        print(f'Error fetching subtitles: {e}')
        return JsonResponse({"error": "Error fetching transcript"}, status=500)
