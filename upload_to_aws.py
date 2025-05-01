import awswrangler as wr
from random_user_api import results_df
from aws_session import aws_session


wr.s3.to_csv(
    df=results_df(),
    path="s3://toludebuckets/random_users_api/results",
    boto3_session=aws_session(),
    mode="append",
    dataset=True
    )



def upload_to_aws():
    wr.s3.to_csv(
    df=results_df(),
    path="s3://toludebuckets/random_users_api/results",
    boto3_session=aws_session(),
    mode="append",
    dataset=True
    )

    return


