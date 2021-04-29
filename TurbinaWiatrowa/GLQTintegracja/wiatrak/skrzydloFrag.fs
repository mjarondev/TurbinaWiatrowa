
#version 330
in vec2 texCoordsFrag;
in vec3 fragNormals;
uniform sampler2D samplerTexture;

out vec4 outColor;
void main()
{
    vec3 ambientLightIntensity = vec3(0.3f, 0.2f, 0.4f);
    vec3 sunLightIntensity = vec3(0.9f, 0.9f, 0.9f);
    vec3 sunLightDirection = normalize(vec3(0.0f, 0.0f, -10.0f));

    vec4 texel = texture(samplerTexture, texCoordsFrag);

    vec3 lightIntensity = ambientLightIntensity + sunLightIntensity * max(dot(fragNormals, sunLightDirection), 0.0f);

    outColor = vec4(texel.rgb * lightIntensity, texel.a);
}