from rest_framework.views import APIView
import boto3
import base64
import boto3
import uuid
from serpapi import GoogleSearch
from snapshot import response
from snapshot.settings import (
    S3_BUCKET_SNAPSHOT_PATH,
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    AWS_S3_REGION_NAME,
    S3_BUCKET_NAME,
    SERP_GOOGLE_LENS_API_KEY,
    env,
)


# Initialize Boto3 client for S3
s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_S3_REGION_NAME,
)


class UploadAndSearchView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            # Decode the base64 image
            data = request.POST.get("image")
            if not data:
                return response.BadRequest({"error": "No image provided"})

            image_data = base64.b64decode(data)
            image_name = S3_BUCKET_SNAPSHOT_PATH + f"{uuid.uuid4()}.png"

            # Save the image to S3
            s3_client.put_object(
                Bucket=S3_BUCKET_NAME,
                Key=image_name,
                Body=image_data,
                ContentType="image/png",
            )

            # Generate a pre-signed URL
            url = s3_client.generate_presigned_url(
                "get_object",
                Params={"Bucket": S3_BUCKET_NAME, "Key": image_name},
                ExpiresIn=3600,
            )

            # Use the GoogleSearch API
            params = {
                "engine": "google_lens",
                "url": url,
                "api_key": SERP_GOOGLE_LENS_API_KEY,
            }

            search = GoogleSearch(params)
            results = search.get_dict()
            visual_matches = results.get("visual_matches", [])

            return response.Ok({"visual_matches": visual_matches})

        except Exception as e:
            return response.InternalServerError({"error": str(e)})
