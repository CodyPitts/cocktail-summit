from django_medusa.renderers import StaticSiteRenderer
from cocktail_summit.models import Speaker, Sponsor, Session

class HomeRenderer(StaticSiteRenderer):
    def get_paths(self):
        return frozenset([
            "/",
        ])


class SpeakerRenderer(StaticSiteRenderer):
    def get_paths(self):
        return frozenset([
            "/speakers/",
        ])


class SponsorRenderer(StaticSiteRenderer):
    def get_paths(self):
        return frozenset([
            "/sponsors/",
        ])


class SessionRenderer(StaticSiteRenderer):
    def get_paths(self):
        return frozenset([
            "/schedule/",
        ])

renderers = [HomeRenderer, SpeakerRenderer, SponsorRenderer, SessionRenderer]









