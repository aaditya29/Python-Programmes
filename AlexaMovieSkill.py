# -*- coding: utf-8 -*-
"""Simple fact sample app."""

import random
import logging

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import (
    AbstractRequestHandler, AbstractExceptionHandler,
    AbstractRequestInterceptor, AbstractResponseInterceptor)
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response


# =========================================================================================================================================
# TODO: The items below this comment need your attention.
# =========================================================================================================================================
SKILL_NAME = "Movie Facts"
GET_FACT_MESSAGE = "Here's your trending fact: "
HELP_MESSAGE = "You can say tell me a movie fact, or, you can say exit... What can I help you with?"
HELP_REPROMPT = "What can I help you with?"
STOP_MESSAGE = "Goodbye!"
FALLBACK_MESSAGE = "The Movie Facts skill can't help you with that.  It can help you discover facts about movie if you say tell me a movie fact. What can I help you with?"
FALLBACK_REPROMPT = 'What can I help you with?'
EXCEPTION_MESSAGE = "Sorry. I cannot help you with that."

data = [
  'In Gangs of wasseypur 1, you might have noticed this scene, when Shahid khan was working in coal mine and which got flooded. A messenger came with the bad news that shahid khan’s wife is in labor pain and baby got stuck. Shahid khan was not allowed to see her wife. This scene is an Allusion of 1975 Chasnala coal mine tragedy, Dhanbad. The gate was shut so the workers couldn’t evacuate themselves and 370 mine workers got killed.',
  'In Batman VS Superman, Ben Affleck had met Christian Bale in a costume shop and asked for his advice on playing Batman. Coincidentally, both of them were there to buy Batman costume for their sons.',
  'In Guardian Of The Galaxy, Chris Pratt lost 60 pounds (27 kg) in six months to play Star Lord. He also stole the costume of Star Lord from the set so that he could wear it while visiting childrens hospital to cheer them up.',
  'It took five hours to apply the Drax make up and Dave Bautista stood the entire time with no complaints in the Guardian Of The Galaxy.',
  'In the movie Godzilla, Godzilla is present in the film for only 8 minutes.',
  'In the movie 300, The flowing effect of the Oracle dancing scene was accomplished by filming the actress under water.',
  'In the movie Titanic, The filmmakers had only one chance to shoot the scene where water crashes into the Grand Staircase because the entire set would have been destroyed in that shot.',
  'Before the role of Daredevil was given to Ben Affleck, it was offered to his longtime friend Matt Damon.',
  'Leonardo Dicaprio was considered to be cast as the spiderman, but eventually the role went to his childhood friend Toby Maguire',
  'In the movie Interstellar, The screenplay is based on the works of the theoretical physicist Kip Thorne.',
  'For a cornfield scenein the Interstellar, Christopher Nolan used 500 acres of corn, which he had from his producing of Man of Steel (2013).',
  'Murph’s name is said 79 times in the film Interstellar.',
  'Tom Cruise was actually considered for the role of Raj Malhotra played by Shahrukh Khan in ‘Dilwale Dulhania Le Jayenge’! In fact, Saif Ali Khan was the original choice made by the filmmaker before finally settling for SRK!',
  'Actors Patrick Stewart and Ian McKellan had never played a game of chess in their lives until the movie X-Men required them to do so.',
  'Ryan Gosling was cast as Noah in The Notebook because the director wanted someone "not handsome".',
  'Tyler Durden flashes on screen four times before we actually meet him as a character in the Fight Club.',
]

# =========================================================================================================================================
# Editing anything below this line might break your skill.
# =========================================================================================================================================

sb = SkillBuilder()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


# Built-in Intent Handlers
class GetNewFactHandler(AbstractRequestHandler):
    """Handler for Skill Launch and GetNewFact Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("LaunchRequest")(handler_input) or
                is_intent_name("GetNewSpaceFactIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In GetNewFactHandler")

        random_fact = random.choice(data)
        speech = GET_FACT_MESSAGE + random_fact

        handler_input.response_builder.speak(speech).set_card(
            SimpleCard(SKILL_NAME, random_fact))
        return handler_input.response_builder.response


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In HelpIntentHandler")

        handler_input.response_builder.speak(HELP_MESSAGE).ask(
            HELP_REPROMPT).set_card(SimpleCard(
                SKILL_NAME, HELP_MESSAGE))
        return handler_input.response_builder.response


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name("AMAZON.CancelIntent")(handler_input) or
                is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In CancelOrStopIntentHandler")

        handler_input.response_builder.speak(STOP_MESSAGE)
        return handler_input.response_builder.response


class FallbackIntentHandler(AbstractRequestHandler):
    """Handler for Fallback Intent.
    AMAZON.FallbackIntent is only available in en-US locale.
    This handler will not be triggered except in that locale,
    so it is safe to deploy on any locale.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")

        handler_input.response_builder.speak(FALLBACK_MESSAGE).ask(
            FALLBACK_REPROMPT)
        return handler_input.response_builder.response


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In SessionEndedRequestHandler")

        logger.info("Session ended reason: {}".format(
            handler_input.request_envelope.request.reason))
        return handler_input.response_builder.response


# Exception Handler
class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Catch all exception handler, log exception and
    respond with custom message.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.info("In CatchAllExceptionHandler")
        logger.error(exception, exc_info=True)

        handler_input.response_builder.speak(EXCEPTION_MESSAGE).ask(
            HELP_REPROMPT)

        return handler_input.response_builder.response


# Request and Response loggers
class RequestLogger(AbstractRequestInterceptor):
    """Log the alexa requests."""
    def process(self, handler_input):
        # type: (HandlerInput) -> None
        logger.debug("Alexa Request: {}".format(
            handler_input.request_envelope.request))


class ResponseLogger(AbstractResponseInterceptor):
    """Log the alexa responses."""
    def process(self, handler_input, response):
        # type: (HandlerInput, Response) -> None
        logger.debug("Alexa Response: {}".format(response))


# Register intent handlers
sb.add_request_handler(GetNewFactHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())

# Register exception handlers
sb.add_exception_handler(CatchAllExceptionHandler())

# TODO: Uncomment the following lines of code for request, response logs.
# sb.add_global_request_interceptor(RequestLogger())
# sb.add_global_response_interceptor(ResponseLogger())

# Handler name that is used on AWS lambda
lambda_handler = sb.lambda_handler()