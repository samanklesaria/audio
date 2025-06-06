from torio.io import CodecConfig, StreamingMediaDecoder as StreamReader, StreamingMediaEncoder as StreamWriter

from ._effector import AudioEffector
from ._playback import play_audio
from torchaudio._internal.module_utils import dropping_support

CodecConfig.__init__ = dropping_support(CodecConfig.__init__)
StreamReader.__init__ = dropping_support(StreamReader.__init__)
StreamWriter.__init__ = dropping_support(StreamWriter.__init__)

__all__ = [
    "AudioEffector",
    "StreamReader",
    "StreamWriter",
    "CodecConfig",
    "play_audio",
]
