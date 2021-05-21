# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

#### Adicionada biblioteca para comunicação MQTT entre serviços AWS
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
####

#### Trecho para setup dos certificados necessários e da comunicaçao MQTT
# Parameters for AWS IoT MQTT Client.

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

iotThingEndpoint = "URL_ENDPOINT" #  Endpoint do Broker criado na primeira etapa.
iotThingPort = 8883
iotTopic = "PI3Robot-Topic01"
# Endereço dos certificados. Por padrao devem estar inseridos na pasta "certificates".
rootCAPath = "./certificates/root.pem" # localizaçao do certificado Root - adapte se o nome do arquivo for diferente
privateKeyPath = "./certificates/XXXX-private.pem.key" # localizaçao da chave privada "...-private.pem.key"
certificatePath = "./certificates/XXXX-certificate.pem.crt" # localizaçao do certificado "...-certificate.pem.crt"

# Init AWSIoTMQTTClient
skillIoTMQTTClient = AWSIoTMQTTClient("PI3Robot-Publisher01")
skillIoTMQTTClient.configureEndpoint(iotThingEndpoint,iotThingPort)
skillIoTMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)
skillIoTMQTTClient.connect()
logger.info("mqtt connected")
####

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Welcome, you can say Hello or Help. Which would you like to try?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class HelloWorldIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hello World!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

""" Funçoes adicionadas pelo desenvolvedor:
    
    Funçoes de movimento limitado:
    - MoveForwardIntentHandler
    - MoveBackwardIntentHandler
    - TurnLeftIntentHandler
    - TurnRightIntentHandler
    
    Funçoes de movimento permanente:
    - MoveForwardPermanentIntentHandler
    - MoveBackwardPermanentIntentHandler
    - TurnLeftPermanentIntentHandler
    - TurnRightPermanentIntentHandler
    
    Funçoes adicionais:
    - StopMovementIntent
    - ShutdownIntent
"""

class MoveForwardIntentHandler(AbstractRequestHandler):
    """Handler for Move Forward Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("MoveForwardIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Ok, move forward"
        skillIoTMQTTClient.publish(iotTopic, "forward", 1)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class MoveBackwardIntentHandler(AbstractRequestHandler):
    """Handler for Move Backward Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("MoveBackwardIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Ok, move backward"
        skillIoTMQTTClient.publish(iotTopic, "backward", 1)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class TurnLeftIntentHandler(AbstractRequestHandler):
    """Handler for Turn Left Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("TurnLeftIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Ok, turn left"
        skillIoTMQTTClient.publish(iotTopic, "turnleft", 1)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class TurnRightIntentHandler(AbstractRequestHandler):
    """Handler for Turn Right Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("TurnRightIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Ok, turn right"
        skillIoTMQTTClient.publish(iotTopic, "turnright", 1)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class MoveForwardPermanentIntentHandler(AbstractRequestHandler):
    """Handler for Move Forward Permanent Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("MoveForwardPermanentIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Ok, move forward permanent"
        skillIoTMQTTClient.publish(iotTopic, "forwardpermanent", 1)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class MoveBackwardPermanentIntentHandler(AbstractRequestHandler):
    """Handler for Move Backward Permanent Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("MoveBackwardPermanentIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Ok, move backward permanent"
        skillIoTMQTTClient.publish(iotTopic, "backwardpermanent", 1)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class TurnLeftPermanentIntentHandler(AbstractRequestHandler):
    """Handler for Turn Left Permanent Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("TurnLeftPermanentIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Ok, turn left permanent"
        skillIoTMQTTClient.publish(iotTopic, "turnleftpermanent", 1)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class TurnRightPermanentIntentHandler(AbstractRequestHandler):
    """Handler for Turn Right Permanent Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("TurnRightPermanentIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Ok, turn right permanent "
        skillIoTMQTTClient.publish(iotTopic, "turnrightpermanent", 1)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class StopMovementIntentHandler(AbstractRequestHandler):
    """Handler for Stop Movement Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("StopMovementIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Ok, stop movement "
        skillIoTMQTTClient.publish(iotTopic, "stop", 1)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class ShutdownIntentHandler(AbstractRequestHandler):
    """Handler for Shutdown Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ShutdownIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Ok, shut down "
        skillIoTMQTTClient.publish(iotTopic, "shutdown", 1)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


#######################################################
# Adicione funçoes Intent Handlers nessa regiao

#######################################################

class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelloWorldIntentHandler())

sb.add_request_handler(MoveForwardIntentHandler())
sb.add_request_handler(MoveBackwardIntentHandler())
sb.add_request_handler(TurnLeftIntentHandler())
sb.add_request_handler(TurnRightIntentHandler())
sb.add_request_handler(MoveForwardPermanentIntentHandler())
sb.add_request_handler(MoveBackwardPermanentIntentHandler())
sb.add_request_handler(TurnLeftPermanentIntentHandler())
sb.add_request_handler(TurnRightPermanentIntentHandler())

sb.add_request_handler(StopMovementIntentHandler())
sb.add_request_handler(ShutdownIntentHandler())
# Adicione os add_request_handlers para suas novas classes aqui

sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()
