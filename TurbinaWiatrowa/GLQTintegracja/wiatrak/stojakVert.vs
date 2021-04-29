
#version 330
in layout(location = 0) vec3 position;
in layout(location = 1) vec3 texCoords;
in layout(location = 2) vec3 vertNormals;

uniform mat4 rotate;
uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

uniform mat4 light;

out vec2 texCoordsFrag;
out vec3 fragNormals;
void main()
{
    fragNormals = (light * vec4(vertNormals, 0.0f)).xyz;
    gl_Position = projection * view * model * rotate * vec4(position, 1.0f);
    texCoordsFrag = texCoords.xy;
}