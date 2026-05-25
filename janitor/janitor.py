import json
import boto3

from constants import REQUIRED_TAGS, REPORT_JSON, REPORT_MD

ec2 = boto3.client(
    "ec2",
    endpoint_url="http://localhost:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="us-east-1"
)

report = {
    "unattached_ebs": [],
    "stopped_instances": [],
    "unused_eips": [],
    "missing_tags": []
}


def find_stopped_instances():
    response = ec2.describe_instances()

    for reservation in response.get("Reservations", []):
        for instance in reservation.get("Instances", []):
            state = instance.get("State", {}).get("Name")

            if state == "stopped":
                report["stopped_instances"].append(
                    instance["InstanceId"]
                )


def find_unattached_ebs():
    response = ec2.describe_volumes()

    for volume in response.get("Volumes", []):
        attachments = volume.get("Attachments", [])

        if len(attachments) == 0:
            report["unattached_ebs"].append(
                volume["VolumeId"]
            )
def find_unused_eips():
    response = ec2.describe_addresses()

    for address in response.get("Addresses", []):
        if "AssociationId" not in address:
            report["unused_eips"].append(
                address.get("PublicIp")
            )


def check_missing_tags():
    response = ec2.describe_instances()

    for reservation in response.get("Reservations", []):
        for instance in reservation.get("Instances", []):

            tags = {
                tag["Key"]: tag["Value"]
                for tag in instance.get("Tags", [])
            }

            missing = []

            for required in REQUIRED_TAGS:
                if required not in tags:
                    missing.append(required)

            if missing:
                report["missing_tags"].append({
                    "resource": instance["InstanceId"],
                    "missing": missing
                })


def save_json_report():
    with open(REPORT_JSON, "w") as file:
        json.dump(report, file, indent=4)


def save_markdown_report():

    with open(REPORT_MD, "w") as file:

        file.write("# Cost Hygiene Report\n\n")

        file.write("## Unattached EBS Volumes\n")
        file.write(f"{len(report['unattached_ebs'])}\n\n")

        file.write("## Stopped EC2 Instances\n")
        file.write(f"{len(report['stopped_instances'])}\n\n")

        file.write("## Unused Elastic IPs\n")
        file.write(f"{len(report['unused_eips'])}\n\n")

        file.write("## Resources Missing Tags\n")
        file.write(f"{len(report['missing_tags'])}\n")


find_stopped_instances()
find_unattached_ebs()
find_unused_eips()
check_missing_tags()

save_json_report()
save_markdown_report()

print("Cost hygiene scan completed.")
