import boto3
import os

def main():
    print("Sample Bedrock project skeleton")
    # Check AWS creds
    try:
        sts = boto3.client("sts")
        identity = sts.get_caller_identity()
        print("AWS identity OK:", identity.get("Arn"))
    except Exception as e:
        print("AWS check failed — configure AWS credentials (aws configure) or check IAM role/keys.")
        print("Error:", e)

if __name__ == "__main__":
    main()
