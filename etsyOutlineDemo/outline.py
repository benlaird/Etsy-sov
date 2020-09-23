class Outline:
    id = 1
    clusters = {}
    frame = None

    def __init__(self):
        pass

    @classmethod
    def set_clusters(cls, images_clusters):
        Outline.clusters = images_clusters

    @classmethod
    def get_clusters(cls):
        return Outline.clusters

    @classmethod
    def set_frame(cls, frame):
        Outline.frame = frame

    @classmethod
    def get_frame(cls):
        return Outline.frame

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Id: {id} "
