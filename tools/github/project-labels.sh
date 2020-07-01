#!/bin/bash
###############################################################################
#
#                             project-labels.sh
#
# This script copies labels from source project to dest project.
#
###############################################################################

# This script uses the GitHub Labels REST API
# https://developer.github.com/v3/issues/labels/

# Provide a personal access token that can
# access the source and target repositories.
# This is how you authorize with the GitHub API.
# https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line

# ./project-labels.sh \
#    --source-org=bitcoin --source-repo=bitcoin \
#    --target-org=bitcoin-global --target-repo=bitcoin-global \
#    --token=TOKEN
# Ensure to run as CLI
for i in "$@"
do
case $i in
    -so=*|--source-org=*)           SRC_GITHUB_ORG="${i#*=}" 
    shift ;;
    -sr=*|--source-repo=*)          SRC_GITHUB_REPO="${i#*=}"
    shift ;;
    -to=*|--target-org=*)           TGT_GITHUB_ORG="${i#*=}"
    shift ;;
    -tr=*|--target-repo=*)          TGT_GITHUB_REPO="${i#*=}"
    shift ;;
    -t=*|--token=*)                 GITHUB_TOKEN="${i#*=}"
    shift ;;
    *) error "Unknown parameter passed: $i"; exit 1 ;;
esac
done

# ---------------------------------------------------------

# Headers used in curl commands
GH_ACCEPT_HEADER="Accept: application/vnd.github.symmetra-preview+json"
GH_AUTH_HEADER="Authorization: Bearer $GITHUB_TOKEN"

# Bash for-loop over JSON array with jq
# https://starkandwayne.com/blog/bash-for-loop-over-json-array-using-jq/
sourceLabelsJson64=$(curl --silent -H "$GH_ACCEPT_HEADER" -H "$GH_AUTH_HEADER" https://api.github.com/repos/${SRC_GITHUB_ORG}/${SRC_GITHUB_REPO}/labels | jq '[ .[] | { "name": .name, "color": .color, "description": .description } ]' | jq -r '.[] | @base64' )

# for each label from source repo,
# invoke github api to create or update
# the label in the target repo
for sourceLabelJson64 in $sourceLabelsJson64; do

    # base64 decode the json
    sourceLabelJson=$(echo ${sourceLabelJson64} | base64 --decode | jq -r '.')

    # try to create the label
    # POST /repos/:owner/:repo/labels { name, color, description }
    # https://developer.github.com/v3/issues/labels/#create-a-label
    createLabelResponse=$(echo $sourceLabelJson | curl --silent -X POST -d @- -H "$GH_ACCEPT_HEADER" -H "$GH_AUTH_HEADER" https://api.github.com/repos/${TGT_GITHUB_ORG}/${TGT_GITHUB_REPO}/labels)

    # if creation failed then the response doesn't include an id and jq returns 'null'
    createdLabelId=$(echo $createLabelResponse | jq -r '.id')

    # if label wasn't created maybe it's because it already exists, try to update it
    if [ "$createdLabelId" == "null" ]
    then
        updateLabelResponse=$(echo $sourceLabelJson | curl --silent -X PATCH -d @- -H "$GH_ACCEPT_HEADER" -H "$GH_AUTH_HEADER" https://api.github.com/repos/${TGT_GITHUB_ORG}/${TGT_GITHUB_REPO}/labels/$(echo $sourceLabelJson | jq -r '.name | @uri'))
        echo "Update label response:\n"$updateLabelResponse"\n"
    else
        echo "Create label response:\n"$createLabelResponse"\n"
    fi

done
