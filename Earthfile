VERSION 0.8
FROM alpine:latest

echo:
    RUN echo "# Category: General" 
    ARG EARTHLY_CI
    RUN echo "EARTHLY_CI's value is: $EARTHLY_CI" >> args.txt
    ARG EARTHLY_BUILD_SHA
    RUN echo "EARTHLY_BUILD_SHA's value is: $EARTHLY_BUILD_SHA" >> args.txt
    ARG EARTHLY_LOCALLY
    RUN echo "EARTHLY_LOCALLY's value is: $EARTHLY_LOCALLY" >> args.txt
    ARG EARTHLY_PUSH
    RUN echo "EARTHLY_PUSH's value is: $EARTHLY_PUSH" >> args.txt
    ARG EARTHLY_VERSION
    RUN echo "EARTHLY_VERSION's value is: $EARTHLY_VERSION" >> args.txt
    RUN echo "# Category: Target-related" 
    ARG EARTHLY_TARGET_NAME
    RUN echo "EARTHLY_TARGET_NAME's value is: $EARTHLY_TARGET_NAME" >> args.txt
    ARG EARTHLY_TARGET_PROJECT_NO_TAG
    RUN echo "EARTHLY_TARGET_PROJECT_NO_TAG's value is: $EARTHLY_TARGET_PROJECT_NO_TAG" >> args.txt
    ARG EARTHLY_TARGET_PROJECT
    RUN echo "EARTHLY_TARGET_PROJECT's value is: $EARTHLY_TARGET_PROJECT" >> args.txt
    ARG EARTHLY_TARGET_TAG_DOCKER
    RUN echo "EARTHLY_TARGET_TAG_DOCKER's value is: $EARTHLY_TARGET_TAG_DOCKER" >> args.txt
    ARG EARTHLY_TARGET_TAG
    RUN echo "EARTHLY_TARGET_TAG's value is: $EARTHLY_TARGET_TAG" >> args.txt
    ARG EARTHLY_TARGET
    RUN echo "EARTHLY_TARGET's value is: $EARTHLY_TARGET" >> args.txt
    RUN echo "# Category: Git-related" 
    ARG EARTHLY_GIT_AUTHOR
    RUN echo "EARTHLY_GIT_AUTHOR's value is: $EARTHLY_GIT_AUTHOR" >> args.txt
    ARG EARTHLY_GIT_AUTHOR_EMAIL
    RUN echo "EARTHLY_GIT_AUTHOR_EMAIL's value is: $EARTHLY_GIT_AUTHOR_EMAIL" >> args.txt
    ARG EARTHLY_GIT_AUTHOR_NAME
    RUN echo "EARTHLY_GIT_AUTHOR_NAME's value is: $EARTHLY_GIT_AUTHOR_NAME" >> args.txt
    ARG EARTHLY_GIT_CO_AUTHORS
    RUN echo "EARTHLY_GIT_CO_AUTHORS's value is: $EARTHLY_GIT_CO_AUTHORS" >> args.txt
    ARG EARTHLY_GIT_COMMIT_AUTHOR_TIMESTAMP
    RUN echo "EARTHLY_GIT_COMMIT_AUTHOR_TIMESTAMP's value is: $EARTHLY_GIT_COMMIT_AUTHOR_TIMESTAMP" >> args.txt
    ARG EARTHLY_GIT_BRANCH
    RUN echo "EARTHLY_GIT_BRANCH's value is: $EARTHLY_GIT_BRANCH" >> args.txt
    ARG EARTHLY_GIT_COMMIT_TIMESTAMP
    RUN echo "EARTHLY_GIT_COMMIT_TIMESTAMP's value is: $EARTHLY_GIT_COMMIT_TIMESTAMP" >> args.txt
    ARG EARTHLY_GIT_HASH
    RUN echo "EARTHLY_GIT_HASH's value is: $EARTHLY_GIT_HASH" >> args.txt
    ARG EARTHLY_GIT_ORIGIN_URL
    RUN echo "EARTHLY_GIT_ORIGIN_URL's value is: $EARTHLY_GIT_ORIGIN_URL" >> args.txt
    ARG EARTHLY_GIT_PROJECT_NAME
    RUN echo "EARTHLY_GIT_PROJECT_NAME's value is: $EARTHLY_GIT_PROJECT_NAME" >> args.txt
    ARG EARTHLY_GIT_REFS
    RUN echo "EARTHLY_GIT_REFS's value is: $EARTHLY_GIT_REFS" >> args.txt
    ARG EARTHLY_GIT_SHORT_HASH
    RUN echo "EARTHLY_GIT_SHORT_HASH's value is: $EARTHLY_GIT_SHORT_HASH" >> args.txt
    ARG EARTHLY_SOURCE_DATE_EPOCH
    RUN echo "EARTHLY_SOURCE_DATE_EPOCH's value is: $EARTHLY_SOURCE_DATE_EPOCH" >> args.txt
    RUN echo "# Category: Platform-related" 
    ARG NATIVEARCH
    RUN echo "NATIVEARCH's value is: $NATIVEARCH" >> args.txt
    ARG NATIVEOS
    RUN echo "NATIVEOS's value is: $NATIVEOS" >> args.txt
    ARG NATIVEPLATFORM
    RUN echo "NATIVEPLATFORM's value is: $NATIVEPLATFORM" >> args.txt
    ARG NATIVEVARIANT
    RUN echo "NATIVEVARIANT's value is: $NATIVEVARIANT" >> args.txt
    ARG TARGETARCH
    RUN echo "TARGETARCH's value is: $TARGETARCH" >> args.txt
    ARG TARGETOS
    RUN echo "TARGETOS's value is: $TARGETOS" >> args.txt
    ARG TARGETPLATFORM
    RUN echo "TARGETPLATFORM's value is: $TARGETPLATFORM" >> args.txt
    ARG TARGETVARIANT
    RUN echo "TARGETVARIANT's value is: $TARGETVARIANT" >> args.txt
    ARG USERARCH
    RUN echo "USERARCH's value is: $USERARCH" >> args.txt
    ARG USEROS
    RUN echo "USEROS's value is: $USEROS" >> args.txt
    ARG USERPLATFORM
    RUN echo "USERPLATFORM's value is: $USERPLATFORM" >> args.txt
    ARG USERVARIANT
    RUN echo "USERVARIANT's value is: $USERVARIANT" >> args.txt
    SAVE ARTIFACT args.txt AS LOCAL args.txt
