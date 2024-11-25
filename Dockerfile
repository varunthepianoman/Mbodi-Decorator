FROM osrf/ros:jazzy-desktop

COPY decorator-package /

RUN apt-get update && apt-get install -y x11-apps && apt-get update

COPY docker_entrypoint.bash /docker_entrypoint.bash
RUN chmod +x /docker_entrypoint.bash

ENTRYPOINT ["/docker_entrypoint.bash"]
CMD ["bash"]
