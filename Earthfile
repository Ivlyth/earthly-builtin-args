# GENERATE AT 2024-07-14T00:05:58.574265Z
VERSION 0.8
FROM alpine:latest

echo:
    ARG output=builtin-args.md
    RUN echo "## Category: General" >> $output
    RUN echo "| ARG Name | ARG Value |" >> $output
    RUN echo "|----------|-----------|" >> $output
    ARG EARTHLY_CI
    RUN echo "| EARTHLY_CI | $EARTHLY_CI |" >> $output
    ARG EARTHLY_BUILD_SHA
    RUN echo "| EARTHLY_BUILD_SHA | $EARTHLY_BUILD_SHA |" >> $output
    ARG EARTHLY_LOCALLY
    RUN echo "| EARTHLY_LOCALLY | $EARTHLY_LOCALLY |" >> $output
    ARG EARTHLY_PUSH
    RUN echo "| EARTHLY_PUSH | $EARTHLY_PUSH |" >> $output
    ARG EARTHLY_VERSION
    RUN echo "| EARTHLY_VERSION | $EARTHLY_VERSION |" >> $output
    RUN echo "## Category: Target-related" >> $output
    RUN echo "| ARG Name | ARG Value |" >> $output
    RUN echo "|----------|-----------|" >> $output
    ARG EARTHLY_TARGET_NAME
    RUN echo "| EARTHLY_TARGET_NAME | $EARTHLY_TARGET_NAME |" >> $output
    ARG EARTHLY_TARGET_PROJECT_NO_TAG
    RUN echo "| EARTHLY_TARGET_PROJECT_NO_TAG | $EARTHLY_TARGET_PROJECT_NO_TAG |" >> $output
    ARG EARTHLY_TARGET_PROJECT
    RUN echo "| EARTHLY_TARGET_PROJECT | $EARTHLY_TARGET_PROJECT |" >> $output
    ARG EARTHLY_TARGET_TAG_DOCKER
    RUN echo "| EARTHLY_TARGET_TAG_DOCKER | $EARTHLY_TARGET_TAG_DOCKER |" >> $output
    ARG EARTHLY_TARGET_TAG
    RUN echo "| EARTHLY_TARGET_TAG | $EARTHLY_TARGET_TAG |" >> $output
    ARG EARTHLY_TARGET
    RUN echo "| EARTHLY_TARGET | $EARTHLY_TARGET |" >> $output
    RUN echo "## Category: Git-related" >> $output
    RUN echo "| ARG Name | ARG Value |" >> $output
    RUN echo "|----------|-----------|" >> $output
    ARG EARTHLY_GIT_AUTHOR
    RUN echo "| EARTHLY_GIT_AUTHOR | $EARTHLY_GIT_AUTHOR |" >> $output
    ARG EARTHLY_GIT_AUTHOR_EMAIL
    RUN echo "| EARTHLY_GIT_AUTHOR_EMAIL | $EARTHLY_GIT_AUTHOR_EMAIL |" >> $output
    ARG EARTHLY_GIT_AUTHOR_NAME
    RUN echo "| EARTHLY_GIT_AUTHOR_NAME | $EARTHLY_GIT_AUTHOR_NAME |" >> $output
    ARG EARTHLY_GIT_CO_AUTHORS
    RUN echo "| EARTHLY_GIT_CO_AUTHORS | $EARTHLY_GIT_CO_AUTHORS |" >> $output
    ARG EARTHLY_GIT_COMMIT_AUTHOR_TIMESTAMP
    RUN echo "| EARTHLY_GIT_COMMIT_AUTHOR_TIMESTAMP | $EARTHLY_GIT_COMMIT_AUTHOR_TIMESTAMP |" >> $output
    ARG EARTHLY_GIT_BRANCH
    RUN echo "| EARTHLY_GIT_BRANCH | $EARTHLY_GIT_BRANCH |" >> $output
    ARG EARTHLY_GIT_COMMIT_TIMESTAMP
    RUN echo "| EARTHLY_GIT_COMMIT_TIMESTAMP | $EARTHLY_GIT_COMMIT_TIMESTAMP |" >> $output
    ARG EARTHLY_GIT_HASH
    RUN echo "| EARTHLY_GIT_HASH | $EARTHLY_GIT_HASH |" >> $output
    ARG EARTHLY_GIT_ORIGIN_URL
    RUN echo "| EARTHLY_GIT_ORIGIN_URL | $EARTHLY_GIT_ORIGIN_URL |" >> $output
    ARG EARTHLY_GIT_PROJECT_NAME
    RUN echo "| EARTHLY_GIT_PROJECT_NAME | $EARTHLY_GIT_PROJECT_NAME |" >> $output
    ARG EARTHLY_GIT_REFS
    RUN echo "| EARTHLY_GIT_REFS | $EARTHLY_GIT_REFS |" >> $output
    ARG EARTHLY_GIT_SHORT_HASH
    RUN echo "| EARTHLY_GIT_SHORT_HASH | $EARTHLY_GIT_SHORT_HASH |" >> $output
    ARG EARTHLY_SOURCE_DATE_EPOCH
    RUN echo "| EARTHLY_SOURCE_DATE_EPOCH | $EARTHLY_SOURCE_DATE_EPOCH |" >> $output
    RUN echo "## Category: Platform-related" >> $output
    RUN echo "| ARG Name | ARG Value |" >> $output
    RUN echo "|----------|-----------|" >> $output
    ARG NATIVEARCH
    RUN echo "| NATIVEARCH | $NATIVEARCH |" >> $output
    ARG NATIVEOS
    RUN echo "| NATIVEOS | $NATIVEOS |" >> $output
    ARG NATIVEPLATFORM
    RUN echo "| NATIVEPLATFORM | $NATIVEPLATFORM |" >> $output
    ARG NATIVEVARIANT
    RUN echo "| NATIVEVARIANT | $NATIVEVARIANT |" >> $output
    ARG TARGETARCH
    RUN echo "| TARGETARCH | $TARGETARCH |" >> $output
    ARG TARGETOS
    RUN echo "| TARGETOS | $TARGETOS |" >> $output
    ARG TARGETPLATFORM
    RUN echo "| TARGETPLATFORM | $TARGETPLATFORM |" >> $output
    ARG TARGETVARIANT
    RUN echo "| TARGETVARIANT | $TARGETVARIANT |" >> $output
    ARG USERARCH
    RUN echo "| USERARCH | $USERARCH |" >> $output
    ARG USEROS
    RUN echo "| USEROS | $USEROS |" >> $output
    ARG USERPLATFORM
    RUN echo "| USERPLATFORM | $USERPLATFORM |" >> $output
    ARG USERVARIANT
    RUN echo "| USERVARIANT | $USERVARIANT |" >> $output
    SAVE ARTIFACT $output AS LOCAL $output
